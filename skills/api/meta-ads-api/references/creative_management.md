# Meta Ads API — Creative Management Reference

> Reference: [Ad Creative Docs](https://developers.facebook.com/docs/marketing-api/reference/ad-creative)

Creative management is a **multi-step process** across several Graph endpoints. Order matters.

---

## Full Creative Pipeline (Image Ad)

```
1. Upload Image  →  get image hash
2. Create AdCreative  →  get creative_id (uses hash from step 1)
3. Create Ad  →  links creative_id to an AdSet
```

---

## Step 1: Upload an Image (`AdImage`)

**Endpoint**: `POST /act_{ad_account_id}/adimages`

- Upload as **multipart form data** (binary file), not JSON.
- **Always include the file extension** in the filename (`.jpg`, `.png`). Missing extensions cause opaque 400 errors.
- Returns an image **`hash`** — store this, it's needed for the creative.

```python
import requests

def upload_image(ad_account_id, access_token, image_path):
    url = f"https://graph.facebook.com/v21.0/act_{ad_account_id}/adimages"
    
    with open(image_path, 'rb') as img_file:
        filename = image_path.split('/')[-1]  # e.g. "creative_v1.jpg"
        response = requests.post(url, params={"access_token": access_token},
            files={"filename": (filename, img_file, "image/jpeg")}
        )
    
    response.raise_for_status()
    images = response.json().get('images', {})
    # Returns: {"images": {"creative_v1.jpg": {"hash": "abc123...", ...}}}
    return list(images.values())[0]['hash']
```

**Copying images across accounts**: POST to the destination account's `/adimages` endpoint with `source_account_id` and the image `hash`.

---

## Step 1b: Upload a Video (`AdVideo`)

**Endpoint**: `POST /act_{ad_account_id}/advideos`

Videos use a **chunked resumable upload** for large files:

```python
def upload_video(ad_account_id, access_token, video_path, title="Ad Video"):
    url = f"https://graph-video.facebook.com/v21.0/act_{ad_account_id}/advideos"
    
    with open(video_path, 'rb') as video_file:
        response = requests.post(url,
            params={"access_token": access_token},
            data={"title": title},
            files={"source": video_file}
        )
    
    response.raise_for_status()
    return response.json()['id']  # video_id used in AdCreative
```

Note: Large videos (>1GB) should use the **Resumable Upload API** instead.

---

## Step 2: Create an Ad Creative

**Endpoint**: `POST /act_{ad_account_id}/adcreatives`

### Simple Image Creative

```python
def create_image_creative(ad_account_id, access_token, image_hash, page_id,
                           headline, body, link_url):
    url = f"https://graph.facebook.com/v21.0/act_{ad_account_id}/adcreatives"
    
    payload = {
        "access_token": access_token,
        "name": "Creative_v1",
        "object_story_spec": {
            "page_id": page_id,
            "link_data": {
                "image_hash": image_hash,
                "link": link_url,
                "message": body,
                "name": headline
            }
        }
    }
    
    response = requests.post(url, json=payload)
    response.raise_for_status()
    return response.json()['id']  # creative_id
```

### Dynamic / Multi-Asset Creative (`asset_feed_spec`)

Use `asset_feed_spec` when you want Meta's algorithm to test and optimize across multiple headlines, bodies, and images automatically:

```python
payload = {
    "name": "Dynamic Creative v1",
    "asset_feed_spec": {
        "images": [
            {"hash": "hash_for_image_1"},
            {"hash": "hash_for_image_2"}
        ],
        "titles": [
            {"text": "Best Monitors for Design Work"},
            {"text": "Pro-Grade Displays. Free Shipping."}
        ],
        "bodies": [
            {"text": "Shop Iiyama's full range of professional monitors."},
            {"text": "High refresh rate. True color accuracy. Built to last."}
        ],
        "call_to_action_types": ["SHOP_NOW"],
        "link_urls": [{"website_url": "https://example.com/monitors"}]
    }
}
```

---

## Fetching Existing Creatives

**Endpoint**: `GET /{ad_id}/adcreatives`

To retrieve the creative attached to an existing ad (including its image hashes and texts):

```python
def get_ad_creative(ad_id, access_token):
    url = f"https://graph.facebook.com/v21.0/{ad_id}/adcreatives"
    fields = "name,image_url,body,title,object_story_spec,asset_feed_spec"
    
    resp = requests.get(url, params={
        "access_token": access_token,
        "fields": fields
    })
    resp.raise_for_status()
    return resp.json().get('data', [])
```

---

## Preview an Ad Creative

**Endpoint**: `GET /{ad_id}/previews?ad_format=DESKTOP_FEED_STANDARD`

Returns a rendered HTML iframe preview of the ad in a specific placement. Useful for validating creatives before campaigns go live.

Supported `ad_format` values: `DESKTOP_FEED_STANDARD`, `MOBILE_FEED_STANDARD`, `INSTAGRAM_STANDARD`, `AUDIENCE_NETWORK_OUTSTREAM_VIDEO`.

---

## Audience Targeting (AdSet Level)

Audiences are defined when creating or editing an **AdSet**, not the creative. Key targeting fields:

```python
targeting = {
    "age_min": 25,
    "age_max": 54,
    "genders": [1, 2],  # 1=Male, 2=Female
    "geo_locations": {
        "countries": ["PL", "DE"]
    },
    "interests": [
        {"id": "6003348604981", "name": "Photography"}
    ]
}
```

For **Custom Audiences** (website retargeting, customer lists):

- Create via `POST /act_{ad_account_id}/customaudiences`
- Reference by ID in the `targeting.custom_audiences` array
- Note: Error `1870034` ("Custom Audience Terms Not Accepted") requires user to accept TOS in Business Manager before proceeding.

---

## Generative AI Creative Features

The API supports opt-in to Meta's AI-powered creative improvements when creating an Ad or AdCreative:

| Feature | Field | Effect |
|---|---|---|
| Image Expansion | `image_crops` with `expand_image: true` | Fills aspect ratios across placements |
| Text Generation | `text_generation` | Creates variants based on supplied copy |
| Background Generation | `background_customization` | Swaps background for product images |

These features preview in Ads Manager before going live. Advertisers retain approval control.
