# Marketing Commit Convention

We use a modified version of **Conventional Commits** tailored for creative and marketing operations.

## Format

```
<type>(<scope>): <description>

[optional body]
```

## Types

| Type | Description | Examples |
| :--- | :--- | :--- |
| **feat** | New functionality or major asset. | `feat(lp): add countdown timer` |
| **content** | Creative content changes (Copy, Images). | `content(fb-ads): update hook text for Q3 video`, `content(email): swap hero image` |
| **design** | Styles, layout, visual tweaks. | `design(checkout): darken button color`, `design(blog): increase font size` |
| **analytics** | Tracking, Pixels, GTM, GA4. | `analytics(gtm): add add_to_cart event`, `analytics(meta): verify pixel firing` |
| **config** | Account settings, targeting rules. | `config(audience): exclude recent purchasers` |
| **fix** | Bug fixes, typo corrections. | `fix(typo): correct pricing in headline` |
| **chore** | Maintenance, file cleanup. | `chore: delete unused raw assets` |

## Scopes

Use the campaign name, platform, or component:

- `(black-friday)`
- `(meta)`
- `(hero-section)`
- `(retargeting)`

## Examples

- `content(black-friday): final headline approval`
- `design(lp): mobile padding adjustment`
- `analytics(ga4): fix checkout funnel tracking`
