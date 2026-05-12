# Messages, Hints, And Error Shapes

Generated from backend commit `c50dd33d` on 2026-05-05.

## Normalized HTTP Error Envelope

The global exception filter emits this HTTP shape for Nest-handled errors:

```json
{
  "statusCode": 400,
  "message": "Human-readable message",
  "error": "VALIDATION_ERROR",
  "code": "OPTIONAL_FINE_GRAINED_CODE",
  "hint": "Optional agent-facing recovery hint",
  "next": { "options": [], "docs": "optional-doc-anchor" },
  "fields": [],
  "details": {}
}
```

Notes from source: `statusCode` is camelCase in the normalized backend response. Existing skill docs may choose to mention `status_code` only when a specific endpoint DTO uses snake_case.

## StaticErrors

| Code key | Message | Source |
|---|---|---|
| `AI_MODEL_NOT_FOUND` | AI model not found | `src/utils/customException.ts:5` |
| `AI_MODEL_REQUIRES_CATEGORY` | AI model must have at least one category | `src/utils/customException.ts:6` |
| `MULTIPLE_ASSET_NOT_ALLOWED` | Multiple asset not allowed | `src/utils/customException.ts:7` |
| `ASSETS_NOT_READY` | Your media files are not ready yet | `src/utils/customException.ts:8` |
| `ASSET_INTEGRITY_FAILED` | One or more assets failed quality checks | `src/utils/customException.ts:9` |
| `ASSET_INTEGRITY_PENDING` | Asset integrity check not complete — please wait | `src/utils/customException.ts:10` |
| `ASSETS_ALREADY_USED` | Your media files are already used | `src/utils/customException.ts:11` |
| `ALREADY_HAS_DOWNLOAD_LICENSE` | You already have a download license for this listing | `src/utils/customException.ts:12` |
| `BAD_WORD_DETECTED` | Bad word | `src/utils/customException.ts:13` |
| `BUYER_NOT_ONBOARDED` | You need a PayPal Business account connected to purchase ownership of listings. | `src/utils/customException.ts:14` |
| `CANT_BUY_OWN_LISTING` | Cannot buy your own listing | `src/utils/customException.ts:15` |
| `CANT_CANCEL_SUBSCRIPTION` | Cannot cancel subscription | `src/utils/customException.ts:16` |
| `CANT_CHANGE_LISTING_STATUS` | Cannot change listing status | `src/utils/customException.ts:17` |
| `CANT_DOWNLOAD_ASSET` | Cannot download Asset | `src/utils/customException.ts:18` |
| `CANT_REMOVE_ITEM` | Cannot remove the item | `src/utils/customException.ts:19` |
| `CANT_REMOVE_LISTING` | Cannot remove listing | `src/utils/customException.ts:20` |
| `CANT_REMOVE_TOKEN` | Cannot remove Token | `src/utils/customException.ts:21` |
| `CATEGORY_IN_USE` | Category is in use | `src/utils/customException.ts:22` |
| `CHECK_ASSET_MODERATION` | Check moderation tab first | `src/utils/customException.ts:23` |
| `CONFIG_NOT_FOUND` | Config Not Found | `src/utils/customException.ts:24` |
| `DB_QUERY_FAILED` | DB Query failed | `src/utils/customException.ts:25` |
| `DOWNLOADED_MAX` | User reached the download limit | `src/utils/customException.ts:26` |
| `EMAIL_ALREADY_CONFIRMED` | Email is already confirmed | `src/utils/customException.ts:27` |
| `EMAIL_ALREADY_IN_WAITLIST` | Email is already in waitlist | `src/utils/customException.ts:28` |
| `EMAIL_NOT_CONFIRMED` | Email is not confirmed | `src/utils/customException.ts:29` |
| `EMAIL_REGISTERED` | The email is already registered. | `src/utils/customException.ts:30` |
| `INVITE_REGISTERED_EMAIL` | The email you’re trying to invite is already registered. | `src/utils/customException.ts:31` |
| `EMAIL_VERIFICATION_FAILED` | Email verification failed | `src/utils/customException.ts:32` |
| `EXCEED_MAX_PAID_SHARE` | Exceed max paid share per user | `src/utils/customException.ts:33` |
| `EXIST_TRANSACTION` | The transaction exists | `src/utils/customException.ts:34` |
| `FILE_SIZE_EXCEEDED` | File size exceeds the maximum allowed size of 100MB | `src/utils/customException.ts:35` |
| `FOLLOW_REQUEST_FAILED` | Follow request failed | `src/utils/customException.ts:36` |
| `INVALID_AMOUNT` | Invalid amount | `src/utils/customException.ts:37` |
| `INVALID_EMAIL` | Email doesn't exist | `src/utils/customException.ts:38` |
| `INVALID_INVITE_CODE` | Invalid invite code | `src/utils/customException.ts:39` |
| `INVALID_FILE_EXTENSION` | ZIP bundle must have .zip file extension | `src/utils/customException.ts:40` |
| `INVALID_THUMBNAIL_EXTENSION` | Thumbnail must be .jpg, .jpeg, .png, .gif, .webp, or .avif | `src/utils/customException.ts:41` |
| `INVALID_PARAMETERS` | Invalid parameters received | `src/utils/customException.ts:42` |
| `INVALID_PASSWORD` | Invalid password | `src/utils/customException.ts:43` |
| `INVALID_REFERRAL_CODE` | Invalid referral code | `src/utils/customException.ts:44` |
| `INVALID_SOCIAL_TOKEN` | Invalid Auth0 token | `src/utils/customException.ts:45` |
| `INVALID_TOKEN` | Invalid token | `src/utils/customException.ts:46` |
| `INVALID_TX_HASH` | Invalid Tx Hash | `src/utils/customException.ts:47` |
| `INVALID_URL` | Invalid URL | `src/utils/customException.ts:48` |
| `INVALID_USER_PASS` | Invalid Username and/or Password | `src/utils/customException.ts:49` |
| `INVITE_LIMIT_REACHED` | Invite limit reached. You will be added to the waitlist | `src/utils/customException.ts:50` |
| `INVITE_SAME_USER` | Not allow to invite to your same account. | `src/utils/customException.ts:51` |
| `IPFS_NOT_SAVED` | Ipfs not saved | `src/utils/customException.ts:52` |
| `IPFS_UPLOAD_ERROR` | An error occurred with IPFS | `src/utils/customException.ts:53` |
| `ITEM_NOT_FOUND` | Item not found | `src/utils/customException.ts:54` |
| `KYC_ALREADY_DONE` | KYC is already done | `src/utils/customException.ts:55` |
| `LIKE_LISTING_FAILED` | Like listing failed | `src/utils/customException.ts:56` |
| `MAX_DIRECT_SIGNUP_LIMIT_REACHED` | Max direct signup limit reached. You will be added to the waitlist | `src/utils/customException.ts:57` |
| `MIN_PRICE_TWO_DOLLARS` | Minimum amount is $2.00 | `src/utils/customException.ts:58` |
| `LISTING_IS_NOT_IN_PREMINT` | Listing is not in PREMINT | `src/utils/customException.ts:59` |
| `LISTING_MINT_NOT_ALLOWED` | Minting is not allowed | `src/utils/customException.ts:60` |
| `LISTING_NOT_FOR_SALE` | Listing is not for sale | `src/utils/customException.ts:61` |
| `LISTING_NOT_FOUND` | Listing not found | `src/utils/customException.ts:62` |
| `NON_EXIST_FILE` | The file does not exist | `src/utils/customException.ts:63` |
| `NOT_LISTING_OWNER` | User does not own the listing | `src/utils/customException.ts:64` |
| `NOT_OWNER` | Not Owner | `src/utils/customException.ts:65` |
| `NO_ACTIVE_SUBSCRIPTION` | No active subscription found | `src/utils/customException.ts:66` |
| `NO_BILLING_ACCOUNT` | No billing account found | `src/utils/customException.ts:67` |
| `NO_CHANGES_DETECTED` | No changes was detected | `src/utils/customException.ts:68` |
| `OFFER_EXISTS` | Offer exists | `src/utils/customException.ts:69` |
| `OFFER_NOT_FOUND` | Offer not found | `src/utils/customException.ts:70` |
| `OFFER_PROCESSING` | Offer is being processed | `src/utils/customException.ts:71` |
| `INVALID_OFFER_STATUS` | Offer status does not allow this action | `src/utils/customException.ts:72` |
| `OFFER_COUNTER_LIMIT_REACHED` | Maximum counter-offer rounds reached | `src/utils/customException.ts:73` |
| `OFFER_EXPIRED` | Offer has expired | `src/utils/customException.ts:74` |
| `PAID_SHARE_NOT_RESET` | Paid share is not reset yet | `src/utils/customException.ts:75` |
| `PARENT_HAS_NO_PARENT` | The selected parent must not have a parent itself | `src/utils/customException.ts:76` |
| `PARENT_NOT_TOP_LEVEL` | parent_id must reference a top-level comment — nested threads are not supported | `src/utils/customException.ts:77` |
| `PASSWORD_RESET_LINK_EXPIRED` | Password reset link is expired | `src/utils/customException.ts:78` |
| `PAYMENT_REQUIRED` | Payment required | `src/utils/customException.ts:79` |
| `PAYPAL_NOT_FOUND` | No PayPal account found for your email | `src/utils/customException.ts:80` |
| `PAYPAY_AUTH_EXPIRED` | PayPal Authorization Expired | `src/utils/customException.ts:81` |
| `REPLY_TO_CROSS_THREAD` | reply_to must reference the parent comment or a reply in the same thread | `src/utils/customException.ts:82` |
| `REPLY_TO_REQUIRES_PARENT` | reply_to requires parent_id — set parent_id to the top-level comment of the thread | `src/utils/customException.ts:83` |
| `REWARD_TYPE_ALREADY_EXISTS` | A reward type with this name already exists | `src/utils/customException.ts:84` |
| `REWARD_TYPE_NOT_FOUND` | Reward Type Not Found | `src/utils/customException.ts:85` |
| `S3_ERROR` | An error occurred with Amazon S3 | `src/utils/customException.ts:86` |
| `SELLER_NOT_REGISTERED` | Please set up your PayPal account to accept offers. | `src/utils/customException.ts:87` |
| `SELLER_NOT_REGISTERED_CUSTOM` | ### is not registered to accept offers. We have sent your offer along with a message inviting them to get on board. | `src/utils/customException.ts:88` |
| `SENDER_REJECTED` | Sender rejected | `src/utils/customException.ts:89` |
| `SESSION_NOT_FOUND` | Session not found | `src/utils/customException.ts:90` |
| `SHARE_NOT_FOUND` | Share not found | `src/utils/customException.ts:91` |
| `SOCIAL_LOGIN_FAILED` | Auth0 login failed | `src/utils/customException.ts:92` |
| `SUBSCRIPTION_ALREADY_ACTIVE` | An active subscription already exists | `src/utils/customException.ts:93` |
| `SUMSUB_API_ERROR` | Couldn't reach SumSub API | `src/utils/customException.ts:94` |
| `TOKEN_EXISTS` | Token exists | `src/utils/customException.ts:95` |
| `TOKEN_NOT_FOUND` | Token not found | `src/utils/customException.ts:96` |
| `TOO_MANY_REQUESTS` | Too many requests, please try again later | `src/utils/customException.ts:97` |
| `UNAUTHORIZED` | Unauthorized | `src/utils/customException.ts:98` |
| `UNSUPPORTED_FILE` | The file type is not supported | `src/utils/customException.ts:99` |
| `USER_2FA_ALREADY_CONFIRMED` | 2FA is already confirmed | `src/utils/customException.ts:100` |
| `USER_2FA_REQUIRED` | Two-factor authentication must be enabled before admin login | `src/utils/customException.ts:101` |
| `USER_NOT_FOUND` | User not found | `src/utils/customException.ts:102` |
| `USER_SHOULD_PREMINT` | User needs to premint | `src/utils/customException.ts:103` |
| `WALLET_ALREADY_TAKEN` | This wallet is already used by another user | `src/utils/customException.ts:104` |
| `WALLET_IS_REQUIRED` | Wallet is required | `src/utils/customException.ts:105` |
| `WALLET_NOT_FOUND` | Wallet not found | `src/utils/customException.ts:106` |
| `WEB3_ISSUE` | Web3 Issue | `src/utils/customException.ts:107` |
| `CANNOT_SWITCH_FREE_BILLING_INTERVAL` | Cannot switch billing interval on a free plan | `src/utils/customException.ts:133` |
| `BILLING_INTERVAL_ALREADY_ACTIVE` | Billing interval is already active | `src/utils/customException.ts:134` |
| `BILLING_PAYMENT_ACTION_REQUIRED` | Payment action required before changing subscription | `src/utils/customException.ts:135` |
| `SUBSCRIPTION_CHANGE_NOT_ALLOWED` | Subscription change is not allowed | `src/utils/customException.ts:136` |
| `WHITELIST_REQUEST_EXISTS` | Whitelist request already exists | `src/utils/customException.ts:108` |
| `WRONG_2FA_CODE` | Wrong 2FA code | `src/utils/customException.ts:109` |
| `WRONG_ASSET_NAME` | Listing name contains disallowed characters | `src/utils/customException.ts:110` |
| `WRONG_LISTING_STATUS` | Wrong listing status | `src/utils/customException.ts:111` |
| `WRONG_PASSWORD` | Password is incorrect | `src/utils/customException.ts:112` |
| `PAYPAL_BILLING_SETUP_FAILED` | PayPal billing agreement setup failed | `src/utils/customException.ts:113` |
| `PAYPAL_PAYMENT_TOKEN_FAILED` | PayPal payment token creation failed | `src/utils/customException.ts:114` |
| `PAYPAL_PAYMENT_FAILED` | PayPal payment failed | `src/utils/customException.ts:115` |
| `SELLER_PAYMENT_NOT_READY` | Seller has not completed payment setup | `src/utils/customException.ts:116` |
| `WRONG_PAYMENT_METHOD` | Wrong payment method | `src/utils/customException.ts:117` |
| `WRONG_USER_NAME` | Username must be 1-20 characters. Only letters, numbers, hyphens, and underscores are allowed. | `src/utils/customException.ts:118` |
| `USER_NAME_ALREADY_SET` | Username has already been set and cannot be changed. | `src/utils/customException.ts:119` |
| `USER_NAME_TAKEN` | Username is already taken | `src/utils/customException.ts:120` |
| `WRONG_BIO_LENGTH` | Bio must be at most 175 characters | `src/utils/customException.ts:121` |
| `LISTING_NAME_TAKEN` | A listing with this name already exists | `src/utils/customException.ts:122` |
| `WRONG_USER_NAME_LENGTH` | Title must be at most 50 characters | `src/utils/customException.ts:123` |
| `REGISTRATION_TOKEN_EXPIRED` | Registration token expired | `src/utils/customException.ts:124` |
| `PRICE_TOO_LOW_FOR_FEES` | Price is too low to cover platform and payment fees | `src/utils/customException.ts:125` |
| `FOLDER_CAP_REACHED` | Folder cap reached for your plan | `src/utils/customException.ts:127` |
| `LISTING_TERMINAL_STATE` | Listing is in a terminal state — no edits possible | `src/utils/customException.ts:128` |
| `LISTING_EDIT_WINDOW_EXPIRED` | Listing edit window has expired — only some fields remain editable | `src/utils/customException.ts:129` |
| `PUBLISHED_IMMUTABLE` | Published listings are permanent and cannot be deleted | `src/utils/customException.ts:130` |
| `OPERATOR_MANAGED_BILLING` | Billing is managed by your operator | `src/utils/customException.ts:131` |
| `CANNOT_FOLLOW_SELF` | You cannot follow yourself | `src/utils/customException.ts:132` |
| `FOLLOW_TARGET_NOT_FOUND` | The user you are trying to follow does not exist | `src/utils/customException.ts:133` |
| `REVIEW_ACK_REQUIRED` | Account is under review — resend with acknowledge_review: true to proceed | `src/utils/customException.ts:134` |

## Recovery Codes And Hints

| Key | Value | Source |
|---|---|---|
| `code` | EXPORT_TIMEOUT | `src/analytics/classify-export-failure.ts:30` |
| `hint` | Export exceeded the worker deadline. Rerun with a narrower date window or fewer listing ids. | `src/analytics/classify-export-failure.ts:31` |
| `code` | EXPORT_ROW_LIMIT | `src/analytics/classify-export-failure.ts:41` |
| `hint` | Export exceeded the maximum row count. Tighten the date range or add listing id filters and retry. | `src/analytics/classify-export-failure.ts:42` |
| `code` | EXPORT_AUTH | `src/analytics/classify-export-failure.ts:50` |
| `hint` | Upstream rejected the export request (auth/permission). Confirm the account is in good standing, then retry. | `src/analytics/classify-export-failure.ts:51` |
| `code` | EXPORT_UPSTREAM | `src/analytics/classify-export-failure.ts:61` |
| `hint` | An upstream dependency (storage / database) failed. Retry the export; if it keeps failing, wait a few minutes. | `src/analytics/classify-export-failure.ts:62` |
| `code` | EXPORT_UNKNOWN | `src/analytics/classify-export-failure.ts:67` |
| `hint` | Export failed for an unclassified reason. Retry once; if it keeps failing, surface to the operator. | `src/analytics/classify-export-failure.ts:68` |
| `code` | WEAK_PASSWORD | `src/auth/middleware/password-strength.middleware.ts:54` |
| `code` | INSUFFICIENT_CREDITS | `src/billing/interceptors/credit.interceptor.ts:59` |
| `code` | PAYPAL_NOT_CONNECTED | `src/listing/listing.service.ts:2592` |
| `code` | PAYPAL_TOKEN_EXPIRED | `src/listing/listing.service.ts:2604` |
| `code` | VALIDATION_ERROR | `src/listing/listing.service.ts:310` |
| `code` | NO_AUTHORIZATION | `src/paypal/paypal.service.ts:943` |
| `code` | NO_AUTHORIZATION | `src/paypal/paypal.service.ts:987` |
| `code` | VALIDATION_ERROR | `src/utils/agent-validation.pipe.ts:38` |
| `code` | CANNOT_FOLLOW_SELF | `src/utils/error-recovery.ts:114` |
| `hint` | You can only follow other users. Pick a different user id. | `src/utils/error-recovery.ts:115` |
| `code` | FOLLOW_TARGET_NOT_FOUND | `src/utils/error-recovery.ts:122` |
| `hint` | The user id does not match any account. Confirm the id via GET /api/v1/agents/marketplace/users/search?q=<handle>. | `src/utils/error-recovery.ts:123` |
| `code` | REVIEW_ACK_REQUIRED | `src/utils/error-recovery.ts:138` |
| `hint` | Your account is under review. Listings created from this account require admin approval before minting. Resend POST /api/v1/agents/listings with acknowledge_review: true to create the draft anyway. | `src/utils/error-recovery.ts:139` |
| `code` | FOLDER_CAP_REACHED | `src/utils/error-recovery.ts:50` |
| `hint` | Delete a folder of this type, or upgrade your plan. See `next.options` for the right endpoint based on your current plan, and `details` for your plan, cap, and current count. | `src/utils/error-recovery.ts:51` |
| `code` | LISTING_TERMINAL_STATE | `src/utils/error-recovery.ts:74` |
| `hint` | No edits are possible on this listing. Read `details.current_status` to see why. Create a new listing if changes are needed. | `src/utils/error-recovery.ts:75` |
| `code` | LISTING_EDIT_WINDOW_EXPIRED | `src/utils/error-recovery.ts:82` |
| `hint` | The 15-minute post-create edit window has passed. Read `details.editable_fields` for the narrow set that can still be patched. | `src/utils/error-recovery.ts:83` |
| `code` | PUBLISHED_IMMUTABLE | `src/utils/error-recovery.ts:90` |
| `hint` | Published listings are permanent. Do not retry — surface this to the operator and create a new listing if a different version is needed. | `src/utils/error-recovery.ts:91` |
| `code` | OPERATOR_MANAGED_BILLING | `src/utils/error-recovery.ts:98` |
| `hint` | Your operator controls billing for this account. Contact them to change plans or review billing state. | `src/utils/error-recovery.ts:99` |
| `code` | NO_ACTIVE_SUBSCRIPTION | `src/utils/error-recovery.ts:112` |
| `hint` | Start a paid subscription before upgrading or switching billing intervals. | `src/utils/error-recovery.ts:113` |
| `code` | SUBSCRIPTION_ALREADY_ACTIVE | `src/utils/error-recovery.ts:134` |
| `hint` | You are already on this plan. Use the interval switch endpoint only if the monthly/yearly billing interval needs to change. | `src/utils/error-recovery.ts:135` |
| `code` | CANNOT_SWITCH_FREE_BILLING_INTERVAL | `src/utils/error-recovery.ts:157` |
| `hint` | Free plans have no billing interval. Start checkout with the desired paid plan and interval. | `src/utils/error-recovery.ts:158` |
| `code` | BILLING_INTERVAL_ALREADY_ACTIVE | `src/utils/error-recovery.ts:179` |
| `hint` | No billing change is needed because this interval is already active. | `src/utils/error-recovery.ts:180` |
| `code` | BILLING_PAYMENT_ACTION_REQUIRED | `src/utils/error-recovery.ts:194` |
| `hint` | Resolve the Stripe payment state before changing the subscription. | `src/utils/error-recovery.ts:195` |
| `code` | SUBSCRIPTION_CHANGE_NOT_ALLOWED | `src/utils/error-recovery.ts:216` |
| `hint` | This subscription change is not available through the requested API action. Check the current subscription before choosing the next billing flow. | `src/utils/error-recovery.ts:217` |
| `code` | INVALID_SOCIAL_TOKEN | `src/utils/errors.ts:5` |
| `code` | SOCIAL_LOGIN_FAILED | `src/utils/errors.ts:9` |
| `code` | UNAUTHENTICATED | `src/utils/gqlAuth.guard.ts:111` |
| `code` | UNAUTHENTICATED | `src/utils/gqlAuth.guard.ts:116` |
| `code` | FORBIDDEN | `src/utils/gqlAuth.guard.ts:126` |
| `code` | RATE_LIMITED | `src/utils/gqlAuth.guard.ts:136` |
| `code` | UNAUTHENTICATED | `src/utils/gqlAuth.guard.ts:141` |
| `code` | FORBIDDEN | `src/utils/gqlAuth.guard.ts:39` |
| `code` | RATE_LIMITED | `src/utils/gqlAuth.guard.ts:88` |
| `code` | UNAUTHENTICATED | `src/utils/gqlAuth.guard.ts:93` |
| `code` | MARKETPLACE_DISABLED | `src/utils/marketplace-enabled.guard.ts:45` |
| `code` | MARKETPLACE_DISABLED | `src/utils/marketplace-enabled.guard.ts:60` |
| `hint` | Commerce endpoints are hidden at launch; see skills/reference.md#marketplace-fields. | `src/utils/marketplace-enabled.guard.ts:62` |
| `code` | SSRF_BLOCKED | `src/webhook/webhook-outbox.handler.ts:100` |

## Explicit Return Messages

| Message | Source |
|---|---|
| OK | `src/activity/activity.mutation.ts:127` |
| OK | `src/activity/activity.mutation.ts:147` |
| OK | `src/activity/activity.mutation.ts:157` |
| OK | `src/activity/activity.mutation.ts:167` |
| OK | `src/activity/activity.mutation.ts:190` |
| OK | `src/activity/activity.mutation.ts:213` |
| OK | `src/activity/activity.mutation.ts:223` |
| OK | `src/activity/activity.mutation.ts:233` |
| OK | `src/activity/activity.mutation.ts:243` |
| OK | `src/activity/activity.mutation.ts:45` |
| OK | `src/activity/activity.mutation.ts:56` |
| OK | `src/activity/activity.mutation.ts:67` |
| Request sent successfully | `src/activity/activity.mutation.ts:89` |
| OK | `src/agent/agent-admin.controller.ts:46` |
| Password reset email sent | `src/agent/agent.service.ts:2603` |
| Password set | `src/agent/agent.service.ts:2641` |
| Verification email sent to new address | `src/agent/agent.service.ts:2699` |
| Verification email sent | `src/agent/agent.service.ts:2733` |
| 2FA disabled | `src/agent/agent.service.ts:2846` |
| Listing unpublished | `src/agent/agent.service.ts:4040` |
| Price updated | `src/agent/agent.service.ts:4080` |
| Listing has been queued for reprocessing | `src/agent/agent.service.ts:4132` |
| This email belongs to an existing account. The account owner must approve the agent upgrade. | `src/agent/agent.service.ts:4218` |
| Device flow completed but API key delivery expired. Use POST /api/v1/agents/api-key/regenerate to get a new key. | `src/agent/agent.service.ts:4281` |
| Auto top-up cancelled | `src/agent/controllers/agent-account.controller.ts:272` |
| Subscription cancelled | `src/agent/controllers/agent-account.controller.ts:331` |
| Bid submitted. You will be notified when it is confirmed on-chain. | `src/agent/controllers/agent-marketplace.controller.ts:284` |
| Bid cancelled | `src/agent/controllers/agent-marketplace.controller.ts:312` |
| OK | `src/agent/controllers/agent-social.controller.ts:239` |
| OK | `src/agent/controllers/agent-social.controller.ts:323` |
| OK | `src/agent/controllers/agent-social.controller.ts:397` |
| Offer cancelled | `src/agent/services/agent-offer.service.ts:102` |
| Offer rejected | `src/agent/services/agent-offer.service.ts:125` |
| Offer created | `src/agent/services/agent-offer.service.ts:45` |
| Counter-offer accepted | `src/agent/services/agent-offer.service.ts:77` |
| Offer accepted | `src/agent/services/agent-offer.service.ts:85` |
| OK | `src/auction/auction.mutation.ts:23` |
| OK | `src/auction/auction.mutation.ts:35` |
| OK | `src/folder/controllers/agent-folder.controller.ts:159` |
| OK | `src/folder/controllers/agent-folder.controller.ts:220` |
| OK | `src/folder/controllers/agent-folder.controller.ts:259` |
| OK | `src/folder/controllers/agent-folder.controller.ts:310` |
| OK | `src/folder/controllers/agent-folder.controller.ts:327` |
| Backfill started | `src/listing/listing-admin.controller.ts:29` |
| OK | `src/listing/listing.mutation.ts:102` |
| OK | `src/listing/listing.mutation.ts:140` |
| OK | `src/listing/listing.mutation.ts:181` |
| OK | `src/listing/listing.mutation.ts:192` |
| OK | `src/listing/listing.mutation.ts:203` |
| OK | `src/listing/listing.mutation.ts:229` |
| OK | `src/listing/listing.mutation.ts:254` |
| OK | `src/listing/listing.mutation.ts:264` |
| OK | `src/listing/listing.mutation.ts:275` |
| OK | `src/listing/listing.mutation.ts:286` |
| OK | `src/listing/listing.mutation.ts:301` |
| OK | `src/listing/listing.mutation.ts:312` |
| OK | `src/listing/listing.mutation.ts:322` |
| OK | `src/listing/listing.mutation.ts:342` |
| OK | `src/listing/listing.mutation.ts:354` |
| OK | `src/listing/listing.mutation.ts:364` |
| OK | `src/listing/listing.mutation.ts:374` |
| OK | `src/listing/listing.mutation.ts:384` |
| OK | `src/listing/listing.mutation.ts:394` |
| OK | `src/listing/listing.mutation.ts:404` |
| OK | `src/listing/listing.mutation.ts:414` |
| OK | `src/listing/listing.mutation.ts:424` |
| OK | `src/listing/listing.mutation.ts:435` |
| OK | `src/listing/listing.mutation.ts:80` |
| OK | `src/listing/listing.service.ts:1125` |
| Publishing in progress | `src/listing/listing.service.ts:1142` |
| Publishing in progress | `src/listing/listing.service.ts:1158` |
| OK | `src/listing/listing.service.ts:1163` |
| Publishing in progress | `src/listing/listing.service.ts:1292` |
| Purchase already in progress | `src/listing/listing.service.ts:2676` |
| Payment is being processed | `src/listing/listing.service.ts:3095` |
| No purchase found for this key | `src/listing/listing.service.ts:3102` |
| OK | `src/marketplace/marketplace.mutation.ts:33` |
| OK | `src/marketplace/marketplace.mutation.ts:46` |
| OK | `src/marketplace/marketplace.mutation.ts:59` |
| OK | `src/marketplace/marketplace.mutation.ts:71` |
| Counter-offer accepted | `src/marketplace/marketplace.mutation.ts:90` |
| Agent has no active operator. Contact admin to assign one before enabling Telegram. | `src/notifications/controllers/telegram.controller.ts:171` |
| Your operator needs to link their Telegram first. Telegram notifications are routed through them. | `src/notifications/controllers/telegram.controller.ts:194` |
| OK | `src/notifications/notifications.mutation.ts:22` |
| Notification setting updated | `src/notifications/notifications.mutation.ts:33` |
| OK | `src/notifications/notifications.mutation.ts:44` |
| Your account access has been restored. | `src/notifications/types/notifications/account.notifications.ts:103` |
| Your account access has been restored. | `src/notifications/types/notifications/account.notifications.ts:111` |
| Your account is fully activated. | `src/notifications/types/notifications/account.notifications.ts:152` |
| Your account is fully activated. | `src/notifications/types/notifications/account.notifications.ts:160` |
| Your 2FA is verified. | `src/notifications/types/notifications/account.notifications.ts:201` |
| Your 2FA is verified. | `src/notifications/types/notifications/account.notifications.ts:209` |
| Your account is temporarily limited due to unusual activity. | `src/notifications/types/notifications/account.notifications.ts:56` |
| Your account is temporarily limited due to unusual activity. | `src/notifications/types/notifications/account.notifications.ts:63` |
| Auction for ${this.listingName} has been canceled. | `src/notifications/types/notifications/auctions.notifications.ts:113` |
| Auction for ${this.listingName} has been canceled. | `src/notifications/types/notifications/auctions.notifications.ts:121` |
| You have purchased ${this.listingName} in Auction. | `src/notifications/types/notifications/auctions.notifications.ts:181` |
| You have purchased ${this.listingName} in Auction. | `src/notifications/types/notifications/auctions.notifications.ts:189` |
| You have received a New Bid for ${this.listingName}. | `src/notifications/types/notifications/auctions.notifications.ts:246` |
| You have received a New Bid for ${this.listingName}. | `src/notifications/types/notifications/auctions.notifications.ts:254` |
| Bid to ${this.listingName} from ${this.bidder} canceled. | `src/notifications/types/notifications/auctions.notifications.ts:307` |
| Bid to ${this.listingName} from ${this.bidder} canceled. | `src/notifications/types/notifications/auctions.notifications.ts:315` |
| You have started a New Auction for ${this.listingName}. | `src/notifications/types/notifications/auctions.notifications.ts:53` |
| You have started a New Auction for ${this.listingName}. | `src/notifications/types/notifications/auctions.notifications.ts:61` |
| ${this.listingName} was denied. Reason: ${this.reason}. | `src/notifications/types/notifications/creator.notifications.ts:117` |
| ${this.listingName} was denied. Reason: ${this.reason}. | `src/notifications/types/notifications/creator.notifications.ts:125` |
| Your creator access has been temporarily paused. | `src/notifications/types/notifications/creator.notifications.ts:183` |
| Your creator access has been temporarily paused. | `src/notifications/types/notifications/creator.notifications.ts:190` |
| Your Create function has been restored. | `src/notifications/types/notifications/creator.notifications.ts:231` |
| Your Create function has been restored. | `src/notifications/types/notifications/creator.notifications.ts:239` |
| The file "${this.assetName}" was approved. | `src/notifications/types/notifications/creator.notifications.ts:48` |
| The file "${this.assetName}" was approved. | `src/notifications/types/notifications/creator.notifications.ts:56` |
| You purchased a download license for ${this.listingName}. | `src/notifications/types/notifications/download-license.notifications.ts:121` |
| You purchased a download license for ${this.listingName}. | `src/notifications/types/notifications/download-license.notifications.ts:129` |
| Someone purchased a download license for ${this.listingName}. | `src/notifications/types/notifications/download-license.notifications.ts:61` |
| Someone purchased a download license for ${this.listingName}. | `src/notifications/types/notifications/download-license.notifications.ts:69` |
| ${this.commenterName} commented on ${this.listingName}. | `src/notifications/types/notifications/engagement.notifications.ts:137` |
| ${this.commenterName} commented on ${this.listingName}. | `src/notifications/types/notifications/engagement.notifications.ts:145` |
| ${this.likerName} liked ${this.listingName}. | `src/notifications/types/notifications/engagement.notifications.ts:207` |
| ${this.likerName} liked ${this.listingName}. | `src/notifications/types/notifications/engagement.notifications.ts:215` |
| ${this.likerName} liked ${this.listingName}. | `src/notifications/types/notifications/engagement.notifications.ts:277` |
| ${this.likerName} liked ${this.listingName}. | `src/notifications/types/notifications/engagement.notifications.ts:285` |
| ${this.saverName} saved ${this.listingName}. | `src/notifications/types/notifications/engagement.notifications.ts:347` |
| ${this.saverName} saved ${this.listingName}. | `src/notifications/types/notifications/engagement.notifications.ts:355` |
| ${this.saverName} saved ${this.listingName}. | `src/notifications/types/notifications/engagement.notifications.ts:417` |
| ${this.saverName} saved ${this.listingName}. | `src/notifications/types/notifications/engagement.notifications.ts:425` |
| ${this.commenterName} commented on ${this.listingName}. | `src/notifications/types/notifications/engagement.notifications.ts:67` |
| ${this.commenterName} commented on ${this.listingName}. | `src/notifications/types/notifications/engagement.notifications.ts:75` |
| The price of ${this.ownerName}'s ${this.listingName} has been changed to ${this.newPrice}. | `src/notifications/types/notifications/follower.notifications.ts:115` |
| The price of ${this.ownerName}'s ${this.listingName} has been changed to ${this.newPrice}. | `src/notifications/types/notifications/follower.notifications.ts:123` |
| ${this.sellerName}'s ${this.listingName} sold. | `src/notifications/types/notifications/follower.notifications.ts:176` |
| ${this.sellerName}'s ${this.listingName} sold. | `src/notifications/types/notifications/follower.notifications.ts:184` |
| ${this.ownerName} has started a new auction for ${this.listingName}. | `src/notifications/types/notifications/follower.notifications.ts:237` |
| ${this.ownerName} has started a new auction for ${this.listingName}. | `src/notifications/types/notifications/follower.notifications.ts:245` |
| ${this.ownerName}'s auction price for ${this.listingName} has been updated. | `src/notifications/types/notifications/follower.notifications.ts:299` |
| ${this.ownerName}'s auction price for ${this.listingName} has been updated. | `src/notifications/types/notifications/follower.notifications.ts:307` |
| ${this.ownerName} listed ${this.listingName}. | `src/notifications/types/notifications/follower.notifications.ts:53` |
| ${this.ownerName} listed ${this.listingName}. | `src/notifications/types/notifications/follower.notifications.ts:61` |
| The price of ${this.listingName} has been changed to ${this.newPrice}. | `src/notifications/types/notifications/listing.notifications.ts:117` |
| The price of ${this.listingName} has been changed to ${this.newPrice}. | `src/notifications/types/notifications/listing.notifications.ts:125` |
| The Auction Price for ${this.listingName} has been updated. | `src/notifications/types/notifications/listing.notifications.ts:178` |
| The Auction Price for ${this.listingName} has been updated. | `src/notifications/types/notifications/listing.notifications.ts:186` |
| You have listed ${this.listingName}. | `src/notifications/types/notifications/listing.notifications.ts:52` |
| You have listed ${this.listingName}. | `src/notifications/types/notifications/listing.notifications.ts:60` |
| Your offer for ${this.listingName} has been accepted. | `src/notifications/types/notifications/offers.notifications.ts:121` |
| Your offer for ${this.listingName} has been accepted. | `src/notifications/types/notifications/offers.notifications.ts:129` |
| The seller countered your offer on ${this.listingName} with $${this.counterPrice}. | `src/notifications/types/notifications/offers.notifications.ts:186` |
| The seller countered your offer on ${this.listingName} with $${this.counterPrice}. | `src/notifications/types/notifications/offers.notifications.ts:194` |
| ${this.offerer} canceled their offer on ${this.listingName}. | `src/notifications/types/notifications/offers.notifications.ts:247` |
| ${this.offerer} canceled their offer on ${this.listingName}. | `src/notifications/types/notifications/offers.notifications.ts:255` |
| Your offer for ${this.listingName} was rejected. | `src/notifications/types/notifications/offers.notifications.ts:303` |
| Your offer for ${this.listingName} was rejected. | `src/notifications/types/notifications/offers.notifications.ts:311` |
| ${this.offerer} sent you an offer for ${this.listingName}. | `src/notifications/types/notifications/offers.notifications.ts:57` |
| ${this.offerer} sent you an offer for ${this.listingName}. | `src/notifications/types/notifications/offers.notifications.ts:65` |
| You sold ${this.listingName}. | `src/notifications/types/notifications/sales.notifications.ts:129` |
| You sold ${this.listingName}. | `src/notifications/types/notifications/sales.notifications.ts:137` |
| ${this.listingName} has been transferred. | `src/notifications/types/notifications/sales.notifications.ts:189` |
| ${this.listingName} has been transferred. | `src/notifications/types/notifications/sales.notifications.ts:197` |
| You just purchased ${this.listingName}. | `src/notifications/types/notifications/sales.notifications.ts:61` |
| You just purchased ${this.listingName}. | `src/notifications/types/notifications/sales.notifications.ts:69` |
| ${this.mentionedByName} mentioned you in a comment. | `src/notifications/types/notifications/social.notifications.ts:117` |
| ${this.mentionedByName} mentioned you in a comment. | `src/notifications/types/notifications/social.notifications.ts:125` |
| ${this.followerName} started following you. | `src/notifications/types/notifications/social.notifications.ts:53` |
| ${this.followerName} started following you. | `src/notifications/types/notifications/social.notifications.ts:61` |
| Your wallet is verified. You can now redeem your rewards. | `src/notifications/types/notifications/wallet.notifications.ts:37` |
| Your wallet is verified. You can now redeem your rewards. | `src/notifications/types/notifications/wallet.notifications.ts:45` |
| Your whitelist request has been rejected. | `src/notifications/types/notifications/whitelist.notifications.ts:101` |
| Your whitelist request is being evaluated. | `src/notifications/types/notifications/whitelist.notifications.ts:35` |
| Your whitelist request is being evaluated. | `src/notifications/types/notifications/whitelist.notifications.ts:39` |
| Your account has been whitelisted. | `src/notifications/types/notifications/whitelist.notifications.ts:66` |
| Your account has been whitelisted. | `src/notifications/types/notifications/whitelist.notifications.ts:70` |
| Your whitelist request has been rejected. | `src/notifications/types/notifications/whitelist.notifications.ts:97` |
| OK | `src/user/user.mutation.ts:134` |
| OK | `src/user/user.mutation.ts:145` |
| OK | `src/user/user.mutation.ts:157` |
| OK | `src/user/user.mutation.ts:168` |
| OK | `src/user/user.mutation.ts:179` |
| OK | `src/user/user.mutation.ts:190` |
| OK | `src/user/user.mutation.ts:205` |
| OK | `src/user/user.mutation.ts:236` |
| Notifications updated successfully | `src/user/user.mutation.ts:247` |
| OK | `src/user/user.mutation.ts:277` |
| OK | `src/user/user.mutation.ts:319` |
| OK | `src/user/user.mutation.ts:360` |
| OK | `src/user/user.mutation.ts:380` |
| OK | `src/user/user.mutation.ts:390` |
| OK | `src/user/user.mutation.ts:399` |
| OK | `src/user/user.mutation.ts:408` |
| Created ${created} registration tokens | `src/user/user.mutation.ts:420` |
| OK | `src/user/user.query.ts:270` |
| OK | `src/user/user.query.ts:279` |
| OK | `src/user/user.service.ts:1042` |
| OK | `src/user/user.service.ts:1075` |
| OK | `src/user/user.service.ts:890` |

## Validation Messages

| Decorator | Message | Source |
|---|---|---|
| `IsString` | contract_type is required and must be a string. Allowed values: 'public_domain', 'non_exclusive'. | `src/agent/dto/create-listing.dto.ts:56` |
| `IsNotEmpty` | contract_type is required and cannot be empty. Allowed values: 'public_domain', 'non_exclusive'. | `src/agent/dto/create-listing.dto.ts:60` |
| `IsIn` | contract_type must be 'public_domain' or 'non_exclusive'. The 'exclusive' license is not currently accepted. | `src/agent/dto/create-listing.dto.ts:64` |
| `Matches` | Invalid thumbnail filename | `src/agent/dto/create-listing.dto.ts:84` |
| `Matches` | Invalid filename | `src/agent/dto/create-listing.dto.ts:91` |
| `Matches` | wallet_address must be a valid Ethereum address | `src/agent/dto/register-agent.dto.ts:108` |
| `Matches` | Name can only contain letters, numbers, spaces, hyphens, and underscores | `src/agent/dto/register-agent.dto.ts:18` |
| `Matches` | Username can only contain letters, numbers, hyphens, and underscores (no spaces) | `src/agent/dto/register-agent.dto.ts:34` |
| `Matches` | wallet_address must be a valid Ethereum address | `src/agent/dto/register-agent.dto.ts:55` |
| `Matches` | Name can only contain letters, numbers, spaces, hyphens, and underscores | `src/agent/dto/register-agent.dto.ts:74` |
| `Matches` | Username can only contain letters, numbers, hyphens, and underscores (no spaces) | `src/agent/dto/register-agent.dto.ts:85` |

## Throw Sites

This table is intentionally source-level. Service methods can be shared by more than one endpoint, so route-specific applicability still needs controller/service tracing.

| Exception | Args / message | Source |
|---|---|---|
| `CustomException` | `StaticErrors.WHITELIST_REQUEST_EXISTS` | `src/activity/activity.service.ts:1285` |
| `CustomException` | `StaticErrors.WALLET_IS_REQUIRED` | `src/activity/activity.service.ts:1293` |
| `CustomException` | `StaticErrors.INVALID_TOKEN` | `src/activity/activity.service.ts:1348` |
| `CustomException` | `StaticErrors.INVALID_TOKEN` | `src/activity/activity.service.ts:1368` |
| `CustomException` | `StaticErrors.ITEM_NOT_FOUND` | `src/activity/activity.service.ts:1427` |
| `CustomException` | `StaticErrors.INVALID_TOKEN` | `src/activity/activity.service.ts:1476` |
| `CustomException` | `StaticErrors.INVALID_TOKEN` | `src/activity/activity.service.ts:1496` |
| `CustomException` | `StaticErrors.INVALID_TOKEN` | `src/activity/activity.service.ts:1552` |
| `CustomException` | `StaticErrors.USER_NOT_FOUND` | `src/activity/activity.service.ts:165` |
| `CustomException` | `StaticErrors.USER_NOT_FOUND` | `src/activity/activity.service.ts:1717` |
| `CustomException` | `StaticErrors.SHARE_NOT_FOUND` | `src/activity/activity.service.ts:1851` |
| `CustomException` | `StaticErrors.USER_NOT_FOUND` | `src/activity/activity.service.ts:186` |
| `CustomException` | `StaticErrors.PAID_SHARE_NOT_RESET` | `src/activity/activity.service.ts:1882` |
| `CustomException` | `StaticErrors.EXCEED_MAX_PAID_SHARE` | `src/activity/activity.service.ts:1888` |
| `CustomException` | `StaticErrors.USER_NOT_FOUND` | `src/activity/activity.service.ts:217` |
| `CustomException` | `StaticErrors.USER_NOT_FOUND` | `src/activity/activity.service.ts:226` |
| `CustomException` | `StaticErrors.CANNOT_FOLLOW_SELF` | `src/activity/activity.service.ts:262` |
| `CustomException` | `StaticErrors.FOLLOW_TARGET_NOT_FOUND \| HttpStatus.NOT_FOUND` | `src/activity/activity.service.ts:268` |
| `CustomException` | `StaticErrors.ITEM_NOT_FOUND` | `src/activity/activity.service.ts:361` |
| `throw` | `error` | `src/activity/activity.service.ts:428` |
| `CustomException` | `StaticErrors.ITEM_NOT_FOUND` | `src/activity/activity.service.ts:436` |
| `CustomException` | `StaticErrors.BAD_WORD_DETECTED` | `src/activity/activity.service.ts:553` |
| `CustomException` | `StaticErrors.ITEM_NOT_FOUND` | `src/activity/activity.service.ts:558` |
| `CustomException` | `StaticErrors.ITEM_NOT_FOUND` | `src/activity/activity.service.ts:570` |
| `CustomException` | `StaticErrors.ITEM_NOT_FOUND` | `src/activity/activity.service.ts:574` |
| `CustomException` | `StaticErrors.ITEM_NOT_FOUND` | `src/activity/activity.service.ts:600` |
| `CustomException` | `StaticErrors.PARENT_NOT_TOP_LEVEL` | `src/activity/activity.service.ts:604` |
| `CustomException` | `StaticErrors.REPLY_TO_REQUIRES_PARENT` | `src/activity/activity.service.ts:611` |
| `CustomException` | `StaticErrors.ITEM_NOT_FOUND` | `src/activity/activity.service.ts:622` |
| `CustomException` | `StaticErrors.REPLY_TO_CROSS_THREAD` | `src/activity/activity.service.ts:629` |
| `CustomException` | `StaticErrors.USER_NOT_FOUND` | `src/activity/activity.service.ts:890` |
| `CustomException` | `StaticErrors.ITEM_NOT_FOUND` | `src/activity/activity.service.ts:909` |
| `CustomException` | `StaticErrors.ITEM_NOT_FOUND` | `src/activity/activity.service.ts:914` |
| `throw` | `error` | `src/activity/view.service.ts:108` |
| `BadRequestException` | `'Invalid state parameter'` | `src/agent/agent.controller.ts:158` |
| `BadRequestException` | `'Missing merchantId or merchantIdInPayPal'` | `src/agent/agent.controller.ts:172` |
| `BadRequestException` | `'Token is required'` | `src/agent/agent.controller.ts:400` |
| `throw` | `error` | `src/agent/agent.service.ts:1001` |
| `InternalServerErrorException` | `'PayPal seller onboarding unavailable. Try again later.'` | `src/agent/agent.service.ts:1005` |
| `BadRequestException` | `'PayPal setup state expired or invalid. Please start again.'` | `src/agent/agent.service.ts:1071` |
| `NotFoundException` | `'Agent not found'` | `src/agent/agent.service.ts:1289` |
| `CustomException` | `StaticErrors.REVIEW_ACK_REQUIRED \| HttpStatus.CONFLICT \| { details: { whitelisted: false, can_proceed: true, appeal_url: '/api/v1/agents/appeal', }, }` | `src/agent/agent.service.ts:1293` |
| `BadRequestException` | ``Price must be 0 (free/no-list) or at least $${MIN_PRICE}`` | `src/agent/agent.service.ts:1315` |
| `InternalServerErrorException` | ``License '${dto.contract_type}' is not configured in the database.`` | `src/agent/agent.service.ts:1339` |
| `BadRequestException` | ``None of the provided subcategories could be resolved: ${dto.subcategories.join(', ')}. Use GET /api/v1/agents/categories for valid subcategories.`` | `src/agent/agent.service.ts:1367` |
| `BadRequestException` | `'At least one tag (sub-subcategory) is required. Use GET /api/v1/agents/categories to see available tags under each subcategory.'` | `src/agent/agent.service.ts:1376` |
| `throw` | `err` | `src/agent/agent.service.ts:1402` |
| `throw` | `err` | `src/agent/agent.service.ts:1446` |
| `throw` | `err` | `src/agent/agent.service.ts:1480` |
| `BadRequestException` | `'Listing not found'` | `src/agent/agent.service.ts:1531` |
| `NotFoundException` | `'Listing not found'` | `src/agent/agent.service.ts:1561` |
| `BadRequestException` | `'No assets linked to this listing'` | `src/agent/agent.service.ts:1572` |
| `BadRequestException` | `'No front cover asset found'` | `src/agent/agent.service.ts:1580` |
| `BadRequestException` | `'Source file not found in storage. Please upload before confirming.'` | `src/agent/agent.service.ts:1593` |
| `BadRequestException` | `'Thumbnail file not found in storage. PUT the thumbnail to the provided upload URL, then retry.'` | `src/agent/agent.service.ts:1611` |
| `throw` | `err` | `src/agent/agent.service.ts:1707` |
| `CustomException` | `StaticErrors.LISTING_TERMINAL_STATE \| HttpStatus.BAD_REQUEST \| { details: { current_status: mapAgentStatus(listing.listingStatusId), editable_fields: [], }, }` | `src/agent/agent.service.ts:1785` |
| `CustomException` | `StaticErrors.LISTING_EDIT_WINDOW_EXPIRED \| HttpStatus.BAD_REQUEST \| { details: { current_status: mapAgentStatus(listing.listingStatusId), locked_at: new Date( new Date(listing.createdAt).getTime() + EDIT_WINDOW_MS, ).toISOString(), lock_window_minutes: 15, editable_fields: ['private',...` | `src/agent/agent.service.ts:1812` |
| `BadRequestException` | ``Price must be 0 (free/no-list) or at least $${MIN_PRICE}`` | `src/agent/agent.service.ts:1854` |
| `CustomException` | `StaticErrors.PUBLISHED_IMMUTABLE \| HttpStatus.FORBIDDEN \| { details: { current_status: mapAgentStatus(listing.listingStatusId) }, }` | `src/agent/agent.service.ts:1931` |
| `throw` | `err` | `src/agent/agent.service.ts:2133` |
| `NotFoundException` | ``No asset found for this R2 key: ${r2Key}`` | `src/agent/agent.service.ts:2463` |
| `NotFoundException` | ``Asset is not linked to any listing (r2Key=${r2Key}, assetId=${asset.assetId})`` | `src/agent/agent.service.ts:2471` |
| `NotFoundException` | `'Agent not found'` | `src/agent/agent.service.ts:2484` |
| `BadRequestException` | `'Appeals are only available for suspended accounts'` | `src/agent/agent.service.ts:2486` |
| `ConflictException` | `'You already have an active appeal'` | `src/agent/agent.service.ts:2496` |
| `BadRequestException` | ``Appeal cooldown active until ${cooldownEnd.toISOString()}. Try again later.`` | `src/agent/agent.service.ts:2510` |
| `NotFoundException` | `'No appeal found'` | `src/agent/agent.service.ts:2538` |
| `NotFoundException` | `'Appeal not found'` | `src/agent/agent.service.ts:2557` |
| `BadRequestException` | `'Appeal already reviewed'` | `src/agent/agent.service.ts:2559` |
| `BadRequestException` | `'Agent not found'` | `src/agent/agent.service.ts:2586` |
| `ForbiddenException` | `'Operator has reached maximum agent slots for their plan. Upgrade to add more agents.'` | `src/agent/agent.service.ts:259` |
| `InternalServerErrorException` | `'Failed to send password reset email'` | `src/agent/agent.service.ts:2594` |
| `BadRequestException` | `'Agent not found'` | `src/agent/agent.service.ts:2614` |
| `BadRequestException` | `'Agent not found'` | `src/agent/agent.service.ts:2653` |
| `BadRequestException` | `'Set a password before changing email'` | `src/agent/agent.service.ts:2660` |
| `ConflictException` | `'Email is already in use'` | `src/agent/agent.service.ts:2667` |
| `BadRequestException` | `'Invalid password'` | `src/agent/agent.service.ts:2680` |
| `InternalServerErrorException` | `'Failed to change email'` | `src/agent/agent.service.ts:2690` |
| `ConflictException` | `'Username is already taken'` | `src/agent/agent.service.ts:270` |
| `BadRequestException` | `'Agent not found'` | `src/agent/agent.service.ts:2709` |
| `BadRequestException` | `'Email is already verified'` | `src/agent/agent.service.ts:2712` |
| `InternalServerErrorException` | `'Failed to send verification email'` | `src/agent/agent.service.ts:2724` |
| `BadRequestException` | `'Agent not found'` | `src/agent/agent.service.ts:2744` |
| `BadRequestException` | `'Set a password before enabling 2FA'` | `src/agent/agent.service.ts:2751` |
| `BadRequestException` | `'2FA is already enabled'` | `src/agent/agent.service.ts:2755` |
| `BadRequestException` | `'Invalid password'` | `src/agent/agent.service.ts:2766` |
| `InternalServerErrorException` | `'Failed to enable 2FA'` | `src/agent/agent.service.ts:2777` |
| `BadRequestException` | `'Agent not found'` | `src/agent/agent.service.ts:2803` |
| `BadRequestException` | `'2FA is not enabled'` | `src/agent/agent.service.ts:2806` |
| `BadRequestException` | `'Invalid password'` | `src/agent/agent.service.ts:2817` |
| `BadRequestException` | `'Invalid 2FA code'` | `src/agent/agent.service.ts:2827` |
| `InternalServerErrorException` | `'Failed to disable 2FA'` | `src/agent/agent.service.ts:2837` |
| `BadRequestException` | `'Agent not found'` | `src/agent/agent.service.ts:2887` |
| `ConflictException` | `'Email is already registered'` | `src/agent/agent.service.ts:290` |
| `BadRequestException` | `'Agent not found'` | `src/agent/agent.service.ts:2914` |
| `throw` | `error` | `src/agent/agent.service.ts:292` |
| `NotFoundException` | `'Session not found'` | `src/agent/agent.service.ts:2920` |
| `BadRequestException` | `'Agent not found'` | `src/agent/agent.service.ts:2979` |
| `BadRequestException` | `'Failed to create agent account'` | `src/agent/agent.service.ts:298` |
| `BadRequestException` | `'No callback_url configured. Update your profile first.'` | `src/agent/agent.service.ts:2982` |
| `BadRequestException` | `'callback_url points to a private/internal address. SSRF blocked.'` | `src/agent/agent.service.ts:2989` |
| `NotFoundException` | `'Listing not found'` | `src/agent/agent.service.ts:3135` |
| `ConflictException` | `'Agent already has a linked operator'` | `src/agent/agent.service.ts:3150` |
| `BadRequestException` | `'Token expired or invalid'` | `src/agent/agent.service.ts:3193` |
| `BadRequestException` | `'Token expired or invalid'` | `src/agent/agent.service.ts:3201` |
| `BadRequestException` | `'Token expired or invalid'` | `src/agent/agent.service.ts:3205` |
| `BadRequestException` | `'Token expired or invalid'` | `src/agent/agent.service.ts:3214` |
| `BadRequestException` | `'Token expired or invalid'` | `src/agent/agent.service.ts:3236` |
| `BadRequestException` | `'Token expired or invalid'` | `src/agent/agent.service.ts:3246` |
| `BadRequestException` | `'Token expired or invalid'` | `src/agent/agent.service.ts:3250` |
| `NotFoundException` | `'Operator user not found'` | `src/agent/agent.service.ts:3257` |
| `BadRequestException` | `'Agent accounts cannot be operators. Only human accounts can claim agent links.'` | `src/agent/agent.service.ts:3260` |
| `ConflictException` | `'Agent already has a linked operator'` | `src/agent/agent.service.ts:3281` |
| `throw` | `err` | `src/agent/agent.service.ts:3283` |
| `ConflictException` | `'Username is already taken'` | `src/agent/agent.service.ts:330` |
| `throw` | `err` | `src/agent/agent.service.ts:332` |
| `NotFoundException` | `'No active operator link'` | `src/agent/agent.service.ts:3346` |
| `NotFoundException` | `'Listing not found'` | `src/agent/agent.service.ts:3463` |
| `NotFoundException` | `'Listing not found'` | `src/agent/agent.service.ts:3501` |
| `NotFoundException` | `'Listing not found'` | `src/agent/agent.service.ts:3507` |
| `NotFoundException` | `'Listing not found'` | `src/agent/agent.service.ts:3555` |
| `NotFoundException` | `'Listing not found'` | `src/agent/agent.service.ts:3836` |
| `BadRequestException` | ``Price must be 0 (free/no-list) or at least $${MIN_PRICE}`` | `src/agent/agent.service.ts:4052` |
| `NotFoundException` | `'Device code not found or expired'` | `src/agent/agent.service.ts:4253` |
| `throw` | `err` | `src/agent/agent.service.ts:4474` |
| `ForbiddenException` | `'Only agent accounts can regenerate API keys'` | `src/agent/agent.service.ts:4518` |
| `NotFoundException` | `'User code not found or expired'` | `src/agent/agent.service.ts:4560` |
| `ForbiddenException` | `'Only the account owner can view this device flow'` | `src/agent/agent.service.ts:4566` |
| `NotFoundException` | ``User ${userId} not found`` | `src/agent/agent.service.ts:465` |
| `NotFoundException` | ``User ${userId} not found`` | `src/agent/agent.service.ts:503` |
| `BadRequestException` | `'Agent not found'` | `src/agent/agent.service.ts:610` |
| `BadRequestException` | `'Agent not found'` | `src/agent/agent.service.ts:663` |
| `CustomException` | `StaticErrors.USER_NAME_ALREADY_SET` | `src/agent/agent.service.ts:674` |
| `ConflictException` | `'Username is already taken'` | `src/agent/agent.service.ts:680` |
| `ConflictException` | `'Username is already taken'` | `src/agent/agent.service.ts:698` |
| `throw` | `err` | `src/agent/agent.service.ts:700` |
| `BadRequestException` | `'Agent not found'` | `src/agent/agent.service.ts:712` |
| `ConflictException` | `'Wallet address is already in use'` | `src/agent/agent.service.ts:718` |
| `BadRequestException` | `'Agent not found'` | `src/agent/agent.service.ts:734` |
| `InternalServerErrorException` | `'Agent account is missing Better Auth ID — contact support'` | `src/agent/agent.service.ts:737` |
| `BadRequestException` | `'No active API key found'` | `src/agent/agent.service.ts:750` |
| `InternalServerErrorException` | `'Key rotation failed — please try again'` | `src/agent/agent.service.ts:780` |
| `BadRequestException` | `'Agent not found'` | `src/agent/agent.service.ts:797` |
| `NotFoundException` | ``User ${userId} not found`` | `src/agent/agent.service.ts:812` |
| `BadRequestException` | `'User is not an agent'` | `src/agent/agent.service.ts:815` |
| `BadRequestException` | `'Agent not found'` | `src/agent/agent.service.ts:872` |
| `BadRequestException` | `'Seller already onboarded.'` | `src/agent/agent.service.ts:878` |
| `BadRequestException` | `'Seller already onboarded.'` | `src/agent/agent.service.ts:895` |
| `throw` | `error` | `src/agent/agent.service.ts:897` |
| `InternalServerErrorException` | `'PayPal seller onboarding unavailable. Try again later.'` | `src/agent/agent.service.ts:900` |
| `BadRequestException` | ``Unknown plan: ${dto.plan}`` | `src/agent/controllers/agent-account.controller.ts:282` |
| `BadRequestException` | `'No active subscription to cancel'` | `src/agent/controllers/agent-account.controller.ts:312` |
| `BadRequestException` | `'No active subscription to cancel'` | `src/agent/controllers/agent-account.controller.ts:318` |
| `BadRequestException` | ``Unknown plan: ${dto.plan}`` | `src/agent/controllers/agent-account.controller.ts:369` |
| `NotFoundException` | `'Notification not found'` | `src/agent/controllers/agent-account.controller.ts:455` |
| `throw` | `err` | `src/agent/controllers/agent-account.controller.ts:457` |
| `HttpException` | `{ statusCode: 501, message: 'Aggregated trade history not yet implemented. Use GET /api/v1/agents/listings/:id/activity for per-listing history.', } \| 501` | `src/agent/controllers/agent-account.controller.ts:475` |
| `CustomException` | `StaticErrors.OPERATOR_MANAGED_BILLING \| HttpStatus.FORBIDDEN` | `src/agent/controllers/agent-account.controller.ts:98` |
| `ForbiddenException` | `'Session required'` | `src/agent/controllers/agent-device.controller.ts:86` |
| `NotFoundException` | `'No active bid found for this listing'` | `src/agent/controllers/agent-marketplace.controller.ts:299` |
| `NotFoundException` | `'No active bid on this listing'` | `src/agent/controllers/agent-marketplace.controller.ts:356` |
| `UnauthorizedException` | `'Invalid API key'` | `src/agent/guards/api-key.guard.ts:103` |
| `UnauthorizedException` | `'Missing X-API-Key header'` | `src/agent/guards/api-key.guard.ts:25` |
| `throw` | `this.rateLimitException(errObj?.details?.tryAgainIn)` | `src/agent/guards/api-key.guard.ts:36` |
| `UnauthorizedException` | `result.error?.message \|\| 'Invalid API key'` | `src/agent/guards/api-key.guard.ts:38` |
| `UnauthorizedException` | `'Invalid API key'` | `src/agent/guards/api-key.guard.ts:64` |
| `UnauthorizedException` | `'Agent account is deactivated'` | `src/agent/guards/api-key.guard.ts:68` |
| `throw` | `error` | `src/agent/guards/api-key.guard.ts:91` |
| `throw` | `this.rateLimitException( (error as any)?.body?.details?.tryAgainIn, )` | `src/agent/guards/api-key.guard.ts:97` |
| `ForbiddenException` | `{ statusCode: 403, error: 'AUCTION_DISABLED', message: 'Auctions are not available at this time', }` | `src/agent/guards/auction-enabled.guard.ts:14` |
| `UnauthorizedException` | `'Invalid session'` | `src/agent/guards/http-session.guard.ts:26` |
| `UnauthorizedException` | `'Authentication required'` | `src/agent/guards/http-session.guard.ts:30` |
| `UnauthorizedException` | `'Invalid internal secret'` | `src/agent/guards/internal-secret.guard.ts:25` |
| `UnauthorizedException` | `'Invalid internal secret'` | `src/agent/guards/internal-secret.guard.ts:35` |
| `UnauthorizedException` | `'PayPal billing agreement required. Visit /api/v1/agents/setup/paypal to connect.'` | `src/agent/guards/paypal-connected.guard.ts:48` |
| `UnauthorizedException` | `'Seller not onboarded. Complete PayPal setup to sell. Visit /api/v1/agents/setup/paypal'` | `src/agent/guards/paypal-seller.guard.ts:76` |
| `ForbiddenException` | `'Authentication required'` | `src/agent/guards/permission.guard.ts:43` |
| `ForbiddenException` | ``Insufficient tier permissions for action: ${action}`` | `src/agent/guards/permission.guard.ts:49` |
| `throw` | `error` | `src/agent/guards/session-or-api-key.guard.ts:38` |
| `throw` | `error` | `src/agent/guards/session-or-api-key.guard.ts:48` |
| `UnauthorizedException` | `'Authentication required (session or x-api-key header)'` | `src/agent/guards/session-or-api-key.guard.ts:50` |
| `HttpException` | `{ statusCode: 402, message: 'Insufficient credits', error: 'INSUFFICIENT_CREDITS', creditsRequired: cost, creditsRemaining: balance, } \| 402` | `src/agent/interceptors/credit-cost.interceptor.ts:67` |
| `throw` | `err` | `src/agent/processors/agent-callback.processor.ts:66` |
| `BadRequestException` | `'Only the listing owner can reject offers'` | `src/agent/services/agent-offer.service.ts:115` |
| `NotFoundException` | `'Offer not found'` | `src/agent/services/agent-offer.service.ts:175` |
| `BadRequestException` | `'Only the offer creator can cancel'` | `src/agent/services/agent-offer.service.ts:98` |
| `Error` | ``Template "${name}" not found`` | `src/agent/templates/template.helper.ts:23` |
| `Error` | ``Unreplaced placeholders in "${name}": ${unreplaced.join(', ')}`` | `src/agent/templates/template.helper.ts:35` |
| `CustomException` | `StaticErrors.AI_MODEL_NOT_FOUND` | `src/ai-model/ai-model.service.ts:103` |
| `CustomException` | `StaticErrors.AI_MODEL_REQUIRES_CATEGORY` | `src/ai-model/ai-model.service.ts:57` |
| `CustomException` | `StaticErrors.AI_MODEL_NOT_FOUND` | `src/ai-model/ai-model.service.ts:77` |
| `CustomException` | `StaticErrors.AI_MODEL_REQUIRES_CATEGORY` | `src/ai-model/ai-model.service.ts:86` |
| `throw` | `error` | `src/analytics/analytics.processor.ts:195` |
| `throw` | `error` | `src/analytics/analytics.processor.ts:52` |
| `BadRequestException` | `'Invalid cursor format'` | `src/analytics/analytics.service.ts:124` |
| `NotFoundException` | `'Creator not found'` | `src/analytics/analytics.service.ts:169` |
| `BadRequestException` | `'Invalid cursor format'` | `src/analytics/analytics.service.ts:187` |
| `BadRequestException` | ``Invalid period: ${period}. Use 7d, 30d, or 90d.`` | `src/analytics/analytics.service.ts:28` |
| `BadRequestException` | `'direction must be "up" or "down"'` | `src/analytics/analytics.service.ts:296` |
| `NotFoundException` | `'Category stats not found'` | `src/analytics/analytics.service.ts:398` |
| `BadRequestException` | ``Invalid sortBy: ${sortBy}`` | `src/analytics/analytics.service.ts:419` |
| `BadRequestException` | ``Invalid sortBy: ${sortBy}`` | `src/analytics/analytics.service.ts:454` |
| `NotFoundException` | `'Listing not found'` | `src/analytics/analytics.service.ts:58` |
| `BadRequestException` | `'Only CSV format is currently supported'` | `src/analytics/analytics.service.ts:632` |
| `BadRequestException` | `'Maximum 100 listing IDs per export'` | `src/analytics/analytics.service.ts:637` |
| `BadRequestException` | ``Max ${MAX_CONCURRENT_EXPORTS_PER_USER} concurrent exports. Wait for current exports to finish.`` | `src/analytics/analytics.service.ts:646` |
| `NotFoundException` | `'Export not found'` | `src/analytics/analytics.service.ts:679` |
| `BadRequestException` | `'timeRange is required'` | `src/analytics/analytics.service.ts:768` |
| `BadRequestException` | ``Invalid timeRange: ${params.timeRange}. Use 1h, 6h, 24h, 7d, or 30d.`` | `src/analytics/analytics.service.ts:772` |
| `BadRequestException` | `'Maximum 10 event types allowed'` | `src/analytics/analytics.service.ts:777` |
| `BadRequestException` | ``Invalid period: ${period}. Use 7d, 30d, 90d, or all.`` | `src/analytics/analytics.service.ts:84` |
| `Error` | `'missing fields'` | `src/analytics/analytics.service.ts:840` |
| `Error` | `'invalid date'` | `src/analytics/analytics.service.ts:844` |
| `BadRequestException` | `'Invalid cursor format'` | `src/analytics/analytics.service.ts:852` |
| `Error` | `'My first Sentry error!'` | `src/app.controller.ts:15` |
| `Error` | ``Query too complex: ${complexity}. Maximum allowed: 500`` | `src/app.module.ts:136` |
| `CustomException` | `StaticErrors.ASSETS_NOT_READY` | `src/asset/asset.service.ts:119` |
| `CustomException` | `StaticErrors.ASSETS_NOT_READY` | `src/asset/asset.service.ts:144` |
| `CustomException` | `StaticErrors.ITEM_NOT_FOUND` | `src/asset/asset.service.ts:160` |
| `Error` | ``Placeholder thumbnail key not configured for family "${family}"`` | `src/asset/asset.service.ts:201` |
| `Error` | ``Placeholder thumbnail object missing at ${bucket}/${placeholderKey}: ${(err as Error).message}`` | `src/asset/asset.service.ts:210` |
| `CustomException` | `StaticErrors.INVALID_PARAMETERS` | `src/asset/asset.service.ts:244` |
| `CustomException` | `StaticErrors.FILE_SIZE_EXCEEDED` | `src/asset/asset.service.ts:256` |
| `CustomException` | `StaticErrors.INVALID_FILE_EXTENSION` | `src/asset/asset.service.ts:263` |
| `CustomException` | `StaticErrors.INVALID_THUMBNAIL_EXTENSION` | `src/asset/asset.service.ts:277` |
| `CustomException` | `StaticErrors.LISTING_NOT_FOUND` | `src/asset/asset.service.ts:289` |
| `CustomException` | `StaticErrors.ITEM_NOT_FOUND` | `src/asset/asset.service.ts:328` |
| `CustomException` | `StaticErrors.ITEM_NOT_FOUND` | `src/asset/asset.service.ts:488` |
| `CustomException` | `StaticErrors.ITEM_NOT_FOUND` | `src/asset/asset.service.ts:561` |
| `CustomException` | `StaticErrors.S3_ERROR` | `src/asset/asset.service.ts:602` |
| `CustomException` | `StaticErrors.ITEM_NOT_FOUND` | `src/auction/auction.service.ts:147` |
| `CustomException` | `StaticErrors.ITEM_NOT_FOUND` | `src/auction/auction.service.ts:155` |
| `CustomException` | `StaticErrors.LISTING_NOT_FOUND` | `src/auction/auction.service.ts:286` |
| `CustomException` | `StaticErrors.LISTING_NOT_FOUND` | `src/auction/auction.service.ts:362` |
| `CustomException` | `StaticErrors.LISTING_NOT_FOUND` | `src/auction/auction.service.ts:411` |
| `CustomException` | `StaticErrors.LISTING_NOT_FOUND` | `src/auction/auction.service.ts:434` |
| `CustomException` | `StaticErrors.LISTING_NOT_FOUND` | `src/auction/auction.service.ts:467` |
| `CustomException` | `StaticErrors.LISTING_NOT_FOUND` | `src/auction/auction.service.ts:534` |
| `CustomException` | `StaticErrors.USER_NOT_FOUND` | `src/auction/auction.service.ts:555` |
| `CustomException` | `StaticErrors.LISTING_NOT_FOUND` | `src/auction/auction.service.ts:644` |
| `CustomException` | `StaticErrors.USER_NOT_FOUND` | `src/auction/auction.service.ts:657` |
| `CustomException` | `StaticErrors.LISTING_NOT_FOUND` | `src/auction/auction.service.ts:734` |
| `CustomException` | `StaticErrors.USER_NOT_FOUND` | `src/auction/auction.service.ts:747` |
| `APIError` | `'FORBIDDEN' \| { message: 'This invite code is assigned to a different email address.', }` | `src/auth/better-auth.config.ts:271` |
| `throw` | `oauthErr` | `src/auth/better-auth.config.ts:294` |
| `APIError` | `'FORBIDDEN' \| { message: 'Registration limit reached. A valid invite code is required to sign up.', }` | `src/auth/better-auth.config.ts:310` |
| `throw` | `err` | `src/auth/better-auth.config.ts:315` |
| `Error` | `'Your access is pending approval. Please wait for your invitation to be confirmed.'` | `src/auth/better-auth.config.ts:489` |
| `APIError` | `'BAD_REQUEST' \| { message: 'userCode is required', }` | `src/auth/plugins/device-ownership.plugin.ts:36` |
| `APIError` | `'UNAUTHORIZED' \| { message: 'Authentication required', }` | `src/auth/plugins/device-ownership.plugin.ts:43` |
| `APIError` | `'NOT_FOUND' \| { message: 'Device registration not found or expired', }` | `src/auth/plugins/device-ownership.plugin.ts:53` |
| `APIError` | `'NOT_FOUND' \| { message: 'Device registration not found or expired', }` | `src/auth/plugins/device-ownership.plugin.ts:64` |
| `APIError` | `'FORBIDDEN' \| { message: 'Only the account owner can approve this device', }` | `src/auth/plugins/device-ownership.plugin.ts:70` |
| `BadRequestException` | `'Invalid webhook signature'` | `src/billing/billing-webhook.controller.ts:46` |
| `UnauthorizedException` | `` | `src/billing/billing.controller.ts:14` |
| `Error` | ``Invalid plan: ${plan}`` | `src/billing/billing.mutation.ts:100` |
| `Error` | `'Cannot downgrade to free — use cancelSubscription instead'` | `src/billing/billing.mutation.ts:103` |
| `Error` | ``Invalid interval: ${interval}. Valid options: monthly, yearly`` | `src/billing/billing.mutation.ts:125` |
| `Error` | ``Invalid top-up tier: ${tier}`` | `src/billing/billing.mutation.ts:151` |
| `Error` | ``Invalid plan: ${plan}. Valid options: pro, founders`` | `src/billing/billing.mutation.ts:31` |
| `Error` | ``Invalid plan: ${plan}`` | `src/billing/billing.mutation.ts:73` |
| `Error` | ``Invalid interval: ${interval}`` | `src/billing/billing.mutation.ts:82` |
| `throw` | `err` | `src/billing/billing.service.ts:1070` |
| `throw` | `err` | `src/billing/billing.service.ts:1121` |
| `Error` | `'Amount must be a positive integer'` | `src/billing/billing.service.ts:1313` |
| `Error` | `'Amount must be a positive integer'` | `src/billing/billing.service.ts:1338` |
| `throw` | `err` | `src/billing/billing.service.ts:242` |
| `throw` | `err` | `src/billing/billing.service.ts:274` |
| `Error` | `'Cannot checkout for free plan'` | `src/billing/billing.service.ts:305` |
| `Error` | `'Active subscription exists. Use upgradeSubscription to change plans, or cancelSubscription first.'` | `src/billing/billing.service.ts:313` |
| `Error` | ``No Stripe price configured for plan: ${plan}`` | `src/billing/billing.service.ts:327` |
| `Error` | `'No active subscription'` | `src/billing/billing.service.ts:416` |
| `Error` | `'Already subscribed to this plan'` | `src/billing/billing.service.ts:418` |
| `Error` | `'Use downgradeSubscription for plan downgrades'` | `src/billing/billing.service.ts:421` |
| `Error` | `'Subscription is already canceled. Please start a new subscription.'` | `src/billing/billing.service.ts:429` |
| `Error` | `'Please resolve your outstanding payment before changing your subscription.'` | `src/billing/billing.service.ts:434` |
| `Error` | ``No price configured for plan: ${newPlan}`` | `src/billing/billing.service.ts:455` |
| `Error` | `'No active subscription'` | `src/billing/billing.service.ts:497` |
| `Error` | `'Cannot switch interval on a free plan'` | `src/billing/billing.service.ts:499` |
| `Error` | ``Already on ${newInterval} billing`` | `src/billing/billing.service.ts:501` |
| `Error` | `'Subscription is already canceled. Please start a new subscription.'` | `src/billing/billing.service.ts:508` |
| `Error` | `'Please resolve your outstanding payment before changing your subscription.'` | `src/billing/billing.service.ts:513` |
| `Error` | ``No ${newInterval} price configured for plan: ${sub.plan}`` | `src/billing/billing.service.ts:534` |
| `Error` | `'No active subscription'` | `src/billing/billing.service.ts:577` |
| `Error` | `'Already on this plan'` | `src/billing/billing.service.ts:578` |
| `Error` | `'Target plan is not a downgrade — use upgradeSubscription'` | `src/billing/billing.service.ts:582` |
| `Error` | `'Cannot downgrade to free — use cancelSubscription instead'` | `src/billing/billing.service.ts:588` |
| `Error` | `'Subscription is already canceled. Please start a new subscription.'` | `src/billing/billing.service.ts:599` |
| `Error` | `'Cannot downgrade a subscription that is pending cancellation. ' + 'Cancel the pending cancellation first, then downgrade.'` | `src/billing/billing.service.ts:608` |
| `Error` | ``No price configured for plan: ${targetPlan}`` | `src/billing/billing.service.ts:634` |
| `throw` | `err` | `src/billing/billing.service.ts:719` |
| `Error` | `'No billing account found'` | `src/billing/billing.service.ts:738` |
| `CustomException` | `StaticErrors.NO_BILLING_ACCOUNT` | `src/billing/billing.service.ts:757` |
| `GraphQLError` | `'Insufficient credits' \| { extensions: { code: 'INSUFFICIENT_CREDITS', status: 402, creditsRequired: cost, creditsRemaining: balance, }, }` | `src/billing/interceptors/credit.interceptor.ts:57` |
| `Error` | `'Credit amount must be positive'` | `src/billing/wallet.service.ts:201` |
| `Error` | `'Credit amount must be positive'` | `src/billing/wallet.service.ts:219` |
| `Error` | ``Minted event not found in receipt ${receipt.transactionHash}`` | `src/blockchain/blockchain-outbox.handler.ts:374` |
| `Error` | ``Mint tx ${listing.mintTxHash} not yet confirmed, will retry`` | `src/blockchain/blockchain-outbox.handler.ts:93` |
| `Error` | ``Minted event not found in receipt ${receipt.transactionHash}. ` + `Events: ${ receipt.events?.map((e: any) => e.event).join(', ') \|\| 'none' }`` | `src/blockchain/blockchain.ts:127` |
| `throw` | `err` | `src/blockchain/blockchain.ts:51` |
| `CustomException` | `StaticErrors.ITEM_NOT_FOUND` | `src/category/category.service.ts:43` |
| `CustomException` | `StaticErrors.INVALID_PARAMETERS` | `src/category/category.service.ts:49` |
| `CustomException` | `StaticErrors.PARENT_HAS_NO_PARENT` | `src/category/category.service.ts:57` |
| `CustomException` | `StaticErrors.ITEM_NOT_FOUND` | `src/category/category.service.ts:73` |
| `CustomException` | `StaticErrors.CATEGORY_IN_USE` | `src/category/category.service.ts:77` |
| `CustomException` | `StaticErrors.CONFIG_NOT_FOUND` | `src/config/config.service.ts:51` |
| `BadRequestException` | `'Invalid cursor'` | `src/feed/feed.service.ts:27` |
| `BadRequestException` | `'Cannot manually add/remove listings from PROFILE folder'` | `src/folder/controllers/agent-folder.controller.ts:209` |
| `BadRequestException` | ``Unsupported folder type: ${_exhaustiveCheck}`` | `src/folder/controllers/agent-folder.controller.ts:214` |
| `BadRequestException` | `'Cannot manually add/remove listings from PROFILE folder'` | `src/folder/controllers/agent-folder.controller.ts:248` |
| `BadRequestException` | ``Unsupported folder type: ${_exhaustiveCheck}`` | `src/folder/controllers/agent-folder.controller.ts:253` |
| `NotFoundException` | ``Collection ${collectionId} not found for user ${userId}`` | `src/folder/services/collection.service.ts:119` |
| `NotFoundException` | ``Listing ${listingId} not found`` | `src/folder/services/collection.service.ts:179` |
| `BadRequestException` | `'Cannot favorite this listing — it is not publicly readable'` | `src/folder/services/collection.service.ts:185` |
| `NotFoundException` | ``Failed to find or create FAVORITES folder for user ${userId}`` | `src/folder/services/collection.service.ts:282` |
| `NotFoundException` | ``Collection ${collectionId} not found for user ${userId}`` | `src/folder/services/collection.service.ts:47` |
| `BadRequestException` | ``Folder ${collectionId} is not a COLLECTION or PLAYLIST`` | `src/folder/services/collection.service.ts:56` |
| `NotFoundException` | ``Listing ${listingId} not found`` | `src/folder/services/collection.service.ts:70` |
| `BadRequestException` | `'Cannot add this listing — it is not publicly readable'` | `src/folder/services/collection.service.ts:76` |
| `BadRequestException` | `'Private listings cannot be added to public folders'` | `src/folder/services/collection.service.ts:85` |
| `NotFoundException` | ``Folder ${folderId} not found`` | `src/folder/services/folder-engagement.service.ts:87` |
| `BadRequestException` | ``Folder ${folderId} is a PROFILE folder and cannot be engaged with`` | `src/folder/services/folder-engagement.service.ts:90` |
| `ForbiddenException` | ``Folder ${folderId} is not engageable by this user`` | `src/folder/services/folder-engagement.service.ts:99` |
| `NotFoundException` | ``Folder ${folderId} not found`` | `src/folder/services/folder-facade.service.ts:1014` |
| `ForbiddenException` | `'You do not own this folder'` | `src/folder/services/folder-facade.service.ts:1018` |
| `BadRequestException` | `'Cannot update a PROFILE folder'` | `src/folder/services/folder-facade.service.ts:125` |
| `BadRequestException` | `'Cannot update a system folder'` | `src/folder/services/folder-facade.service.ts:129` |
| `BadRequestException` | `'Cannot change type of a PORTFOLIO folder'` | `src/folder/services/folder-facade.service.ts:134` |
| `ForbiddenException` | `'Privacy features require a Pro membership.'` | `src/folder/services/folder-facade.service.ts:153` |
| `BadRequestException` | `'Cannot delete a PROFILE folder'` | `src/folder/services/folder-facade.service.ts:208` |
| `BadRequestException` | `'Cannot delete a system folder'` | `src/folder/services/folder-facade.service.ts:212` |
| `NotFoundException` | ``Folder ${folderId} not found`` | `src/folder/services/folder-facade.service.ts:413` |
| `NotFoundException` | ``Folder ${folderId} not found`` | `src/folder/services/folder-facade.service.ts:426` |
| `ForbiddenException` | `'You do not own this folder'` | `src/folder/services/folder-facade.service.ts:428` |
| `NotFoundException` | ``Folder ${folderId} not found`` | `src/folder/services/folder-facade.service.ts:443` |
| `ForbiddenException` | `'Access denied'` | `src/folder/services/folder-facade.service.ts:449` |
| `NotFoundException` | ``Folder ${folderId} not found`` | `src/folder/services/folder-facade.service.ts:658` |
| `ForbiddenException` | `'You do not own this folder'` | `src/folder/services/folder-facade.service.ts:661` |
| `BadRequestException` | `'Cannot bulk add to a PROFILE folder'` | `src/folder/services/folder-facade.service.ts:664` |
| `BadRequestException` | `{ message: 'One or more listings not found or deleted', missing, }` | `src/folder/services/folder-facade.service.ts:680` |
| `ForbiddenException` | `{ message: 'You do not own all of the listings', notOwned, }` | `src/folder/services/folder-facade.service.ts:692` |
| `BadRequestException` | `{ message: 'Private listings cannot be added to public folders', privateListings, }` | `src/folder/services/folder-facade.service.ts:707` |
| `BadRequestException` | `'Cannot manually create a PROFILE folder'` | `src/folder/services/folder-facade.service.ts:74` |
| `NotFoundException` | ``Folder ${folderId} not found`` | `src/folder/services/folder-facade.service.ts:810` |
| `ForbiddenException` | `'You do not own this folder'` | `src/folder/services/folder-facade.service.ts:813` |
| `ForbiddenException` | `'Privacy features require a Pro membership.'` | `src/folder/services/folder-facade.service.ts:86` |
| `CustomException` | `StaticErrors.FOLDER_CAP_REACHED \| HttpStatus.FORBIDDEN \| { details: { plan: sub.plan, folder_type: 'PORTFOLIO', limit: limits.maxPortfolios, current: count, }, }` | `src/folder/services/folder-facade.service.ts:956` |
| `CustomException` | `StaticErrors.FOLDER_CAP_REACHED \| HttpStatus.FORBIDDEN \| { details: { plan: sub.plan, folder_type: type === FolderType.COLLECTION ? 'COLLECTION' : 'PLAYLIST', limit: limits.maxCollections, current: count, }, }` | `src/folder/services/folder-facade.service.ts:988` |
| `BadRequestException` | `'INVALID_REORDER_REFERENCE'` | `src/folder/services/folder-reorder.service.ts:34` |
| `BadRequestException` | `'INVALID_REORDER_REFERENCE'` | `src/folder/services/folder-reorder.service.ts:77` |
| `BadRequestException` | `'INVALID_REORDER_REFERENCE'` | `src/folder/services/folder-reorder.service.ts:88` |
| `Error` | `'Invalid listing alias'` | `src/folder/services/listing-visibility.service.ts:29` |
| `Error` | `'Invalid listing alias'` | `src/folder/services/listing-visibility.service.ts:55` |
| `NotFoundException` | `'Listing is not in any portfolio'` | `src/folder/services/portfolio.service.ts:114` |
| `BadRequestException` | `'You do not own this portfolio'` | `src/folder/services/portfolio.service.ts:118` |
| `NotFoundException` | `'Listing not found'` | `src/folder/services/portfolio.service.ts:46` |
| `BadRequestException` | `'You do not own this listing'` | `src/folder/services/portfolio.service.ts:49` |
| `NotFoundException` | `'Target folder not found'` | `src/folder/services/portfolio.service.ts:57` |
| `BadRequestException` | `'You do not own the target folder'` | `src/folder/services/portfolio.service.ts:60` |
| `BadRequestException` | `'Target folder is not a portfolio'` | `src/folder/services/portfolio.service.ts:63` |
| `BadRequestException` | `'Private listings cannot be added to public portfolios'` | `src/folder/services/portfolio.service.ts:73` |
| `throw` | `err` | `src/folder/services/profile-folder.service.ts:48` |
| `NotFoundException` | ``Profile folder not found for user ${userId}`` | `src/folder/services/profile-folder.service.ts:96` |
| `UnauthorizedException` | `'Invalid session'` | `src/listing/guards/http-admin.guard.ts:23` |
| `UnauthorizedException` | `'Authentication required'` | `src/listing/guards/http-admin.guard.ts:27` |
| `ForbiddenException` | `'Admin access required'` | `src/listing/guards/http-admin.guard.ts:32` |
| `ConflictException` | `'Backfill is already running'` | `src/listing/listing-admin.controller.ts:23` |
| `CustomException` | `StaticErrors.ITEM_NOT_FOUND \| HttpStatus.NOT_FOUND` | `src/listing/listing.query.ts:106` |
| `CustomException` | `StaticErrors.ITEM_NOT_FOUND` | `src/listing/listing.query.ts:124` |
| `CustomException` | `StaticErrors.ITEM_NOT_FOUND` | `src/listing/listing.query.ts:180` |
| `CustomException` | `StaticErrors.ITEM_NOT_FOUND` | `src/listing/listing.query.ts:306` |
| `CustomException` | `StaticErrors.ITEM_NOT_FOUND` | `src/listing/listing.query.ts:91` |
| `CustomException` | `StaticErrors.USER_NOT_FOUND` | `src/listing/listing.service.ts:1021` |
| `CustomException` | `StaticErrors.LISTING_NOT_FOUND` | `src/listing/listing.service.ts:1030` |
| `CustomException` | `StaticErrors.LISTING_NOT_FOUND` | `src/listing/listing.service.ts:1083` |
| `CustomException` | `StaticErrors.NOT_LISTING_OWNER` | `src/listing/listing.service.ts:1086` |
| `CustomException` | `StaticErrors.WEB3_ISSUE` | `src/listing/listing.service.ts:1120` |
| `CustomException` | `StaticErrors.WEB3_ISSUE` | `src/listing/listing.service.ts:1123` |
| `CustomException` | `StaticErrors.CANT_CHANGE_LISTING_STATUS` | `src/listing/listing.service.ts:1165` |
| `CustomException` | `StaticErrors.ASSETS_NOT_READY` | `src/listing/listing.service.ts:1173` |
| `throw` | `err` | `src/listing/listing.service.ts:1286` |
| `CustomException` | `StaticErrors.LISTING_NOT_FOUND` | `src/listing/listing.service.ts:1300` |
| `CustomException` | `StaticErrors.NOT_LISTING_OWNER` | `src/listing/listing.service.ts:1303` |
| `CustomException` | `StaticErrors.WEB3_ISSUE` | `src/listing/listing.service.ts:1310` |
| `CustomException` | `StaticErrors.LISTING_NOT_FOUND` | `src/listing/listing.service.ts:1319` |
| `CustomException` | `StaticErrors.NOT_LISTING_OWNER` | `src/listing/listing.service.ts:1322` |
| `CustomException` | `StaticErrors.WEB3_ISSUE` | `src/listing/listing.service.ts:1347` |
| `CustomException` | `StaticErrors.LISTING_NOT_FOUND` | `src/listing/listing.service.ts:1357` |
| `CustomException` | `StaticErrors.NOT_LISTING_OWNER` | `src/listing/listing.service.ts:1360` |
| `CustomException` | `StaticErrors.INVALID_PARAMETERS` | `src/listing/listing.service.ts:1363` |
| `CustomException` | `StaticErrors.LISTING_NOT_FOUND` | `src/listing/listing.service.ts:1392` |
| `CustomException` | `StaticErrors.LISTING_NOT_FOUND` | `src/listing/listing.service.ts:1478` |
| `CustomException` | `StaticErrors.NOT_LISTING_OWNER` | `src/listing/listing.service.ts:1481` |
| `CustomException` | `StaticErrors.WEB3_ISSUE` | `src/listing/listing.service.ts:1524` |
| `CustomException` | `StaticErrors.CANT_CHANGE_LISTING_STATUS` | `src/listing/listing.service.ts:1744` |
| `CustomException` | `StaticErrors.CHECK_ASSET_MODERATION` | `src/listing/listing.service.ts:1747` |
| `CustomException` | `StaticErrors.CANT_CHANGE_LISTING_STATUS` | `src/listing/listing.service.ts:1796` |
| `CustomException` | `StaticErrors.CHECK_ASSET_MODERATION` | `src/listing/listing.service.ts:1799` |
| `CustomException` | `StaticErrors.CANT_REMOVE_LISTING` | `src/listing/listing.service.ts:1833` |
| `CustomException` | `StaticErrors.CANT_REMOVE_LISTING` | `src/listing/listing.service.ts:1836` |
| `CustomException` | `StaticErrors.CANT_REMOVE_LISTING` | `src/listing/listing.service.ts:1965` |
| `CustomException` | `StaticErrors.LISTING_NOT_FOUND` | `src/listing/listing.service.ts:1992` |
| `CustomException` | `StaticErrors.LISTING_NOT_FOUND` | `src/listing/listing.service.ts:2062` |
| `CustomException` | `StaticErrors.CANT_CHANGE_LISTING_STATUS` | `src/listing/listing.service.ts:2066` |
| `CustomException` | `StaticErrors.LISTING_NOT_FOUND` | `src/listing/listing.service.ts:2089` |
| `CustomException` | `StaticErrors.CANT_DOWNLOAD_ASSET` | `src/listing/listing.service.ts:2097` |
| `CustomException` | `StaticErrors.CANT_DOWNLOAD_ASSET` | `src/listing/listing.service.ts:2124` |
| `CustomException` | `StaticErrors.DOWNLOADED_MAX` | `src/listing/listing.service.ts:2133` |
| `CustomException` | `StaticErrors.INVALID_PARAMETERS \| HttpStatus.BAD_REQUEST` | `src/listing/listing.service.ts:2398` |
| `CustomException` | `StaticErrors.LISTING_NOT_FOUND` | `src/listing/listing.service.ts:2582` |
| `CustomException` | `StaticErrors.CANT_BUY_OWN_LISTING` | `src/listing/listing.service.ts:2585` |
| `GraphQLError` | `'PayPal billing agreement required' \| { extensions: { code: 'PAYPAL_NOT_CONNECTED', status: 402 }, }` | `src/listing/listing.service.ts:2591` |
| `GraphQLError` | `'Payment method expired or revoked. Please re-connect PayPal.' \| { extensions: { code: 'PAYPAL_TOKEN_EXPIRED', status: 402 } }` | `src/listing/listing.service.ts:2602` |
| `CustomException` | `StaticErrors.LISTING_NOT_FOR_SALE` | `src/listing/listing.service.ts:2610` |
| `CustomException` | `StaticErrors.LISTING_NOT_FOR_SALE` | `src/listing/listing.service.ts:2619` |
| `CustomException` | `'Asset not available for ownership transfer' as any` | `src/listing/listing.service.ts:2625` |
| `CustomException` | `'Wallet address required for ownership transfer' as any` | `src/listing/listing.service.ts:2630` |
| `CustomException` | `StaticErrors.SELLER_PAYMENT_NOT_READY \| HttpStatus.UNPROCESSABLE_ENTITY` | `src/listing/listing.service.ts:2686` |
| `CustomException` | `StaticErrors.LISTING_NOT_FOR_SALE` | `src/listing/listing.service.ts:2711` |
| `throw` | `err` | `src/listing/listing.service.ts:2754` |
| `CustomException` | `StaticErrors.USER_NOT_FOUND` | `src/listing/listing.service.ts:278` |
| `throw` | `err` | `src/listing/listing.service.ts:2902` |
| `BadRequestException` | `{ message, error: 'VALIDATION_ERROR', code: 'VALIDATION_ERROR', fields: [ { field: 'name', constraint: 'matches', message, }, ], }` | `src/listing/listing.service.ts:307` |
| `CustomException` | `StaticErrors.ITEM_NOT_FOUND \| HttpStatus.NOT_FOUND` | `src/listing/listing.service.ts:3120` |
| `CustomException` | `StaticErrors.ITEM_NOT_FOUND \| HttpStatus.NOT_FOUND` | `src/listing/listing.service.ts:3174` |
| `CustomException` | `StaticErrors.INVALID_PARAMETERS` | `src/listing/listing.service.ts:321` |
| `CustomException` | `StaticErrors.WRONG_USER_NAME_LENGTH` | `src/listing/listing.service.ts:324` |
| `throw` | `error` | `src/listing/listing.service.ts:328` |
| `CustomException` | `StaticErrors.LISTING_NOT_FOUND` | `src/listing/listing.service.ts:3293` |
| `CustomException` | `StaticErrors.LISTING_NOT_FOUND` | `src/listing/listing.service.ts:3300` |
| `CustomException` | `StaticErrors.LISTING_NOT_FOUND` | `src/listing/listing.service.ts:3315` |
| `CustomException` | `StaticErrors.LISTING_NOT_FOUND` | `src/listing/listing.service.ts:3397` |
| `CustomException` | `StaticErrors.LISTING_NOT_FOUND` | `src/listing/listing.service.ts:359` |
| `CustomException` | `StaticErrors.LISTING_NOT_FOUND` | `src/listing/listing.service.ts:3644` |
| `CustomException` | `StaticErrors.UNAUTHORIZED` | `src/listing/listing.service.ts:3650` |
| `CustomException` | `StaticErrors.LISTING_NOT_FOUND` | `src/listing/listing.service.ts:3686` |
| `CustomException` | `StaticErrors.WRONG_LISTING_STATUS` | `src/listing/listing.service.ts:3697` |
| `CustomException` | `StaticErrors.USER_NOT_FOUND` | `src/listing/listing.service.ts:3709` |
| `CustomException` | `StaticErrors.ASSETS_NOT_READY` | `src/listing/listing.service.ts:378` |
| `CustomException` | `StaticErrors.CHECK_ASSET_MODERATION` | `src/listing/listing.service.ts:390` |
| `CustomException` | `StaticErrors.INVALID_PARAMETERS` | `src/listing/listing.service.ts:579` |
| `CustomException` | `StaticErrors.INVALID_PARAMETERS` | `src/listing/listing.service.ts:582` |
| `ForbiddenException` | `'Privacy features require a Pro membership.'` | `src/listing/listing.service.ts:591` |
| `CustomException` | `StaticErrors.INVALID_PARAMETERS` | `src/listing/listing.service.ts:684` |
| `CustomException` | `StaticErrors.INVALID_PARAMETERS` | `src/listing/listing.service.ts:687` |
| `CustomException` | `StaticErrors.INVALID_PARAMETERS` | `src/listing/listing.service.ts:732` |
| `CustomException` | `StaticErrors.INVALID_PARAMETERS` | `src/listing/listing.service.ts:735` |
| `CustomException` | `StaticErrors.LISTING_NOT_FOUND` | `src/listing/listing.service.ts:767` |
| `CustomException` | `StaticErrors.LISTING_NOT_FOUND` | `src/listing/listing.service.ts:839` |
| `CustomException` | `StaticErrors.ASSET_INTEGRITY_FAILED` | `src/listing/utils/assert-assets-checked.ts:17` |
| `CustomException` | `StaticErrors.ASSET_INTEGRITY_PENDING` | `src/listing/utils/assert-assets-checked.ts:24` |
| `CustomException` | `StaticErrors.LISTING_NOT_FOUND` | `src/marketplace/marketplace.service.ts:1015` |
| `CustomException` | `StaticErrors.WEB3_ISSUE` | `src/marketplace/marketplace.service.ts:1063` |
| `CustomException` | `StaticErrors.OFFER_NOT_FOUND` | `src/marketplace/marketplace.service.ts:1160` |
| `CustomException` | `StaticErrors.INVALID_OFFER_STATUS` | `src/marketplace/marketplace.service.ts:1168` |
| `CustomException` | `StaticErrors.OFFER_EXPIRED` | `src/marketplace/marketplace.service.ts:1171` |
| `CustomException` | `StaticErrors.NOT_OWNER` | `src/marketplace/marketplace.service.ts:1177` |
| `CustomException` | `StaticErrors.SESSION_NOT_FOUND` | `src/marketplace/marketplace.service.ts:1189` |
| `CustomException` | `StaticErrors.SELLER_NOT_REGISTERED` | `src/marketplace/marketplace.service.ts:1197` |
| `CustomException` | `StaticErrors.SELLER_NOT_REGISTERED` | `src/marketplace/marketplace.service.ts:1204` |
| `CustomException` | `StaticErrors.SESSION_NOT_FOUND` | `src/marketplace/marketplace.service.ts:1212` |
| `CustomException` | `StaticErrors.OFFER_PROCESSING` | `src/marketplace/marketplace.service.ts:1219` |
| `CustomException` | `StaticErrors.PAYPAY_AUTH_EXPIRED` | `src/marketplace/marketplace.service.ts:1222` |
| `throw` | `err` | `src/marketplace/marketplace.service.ts:1268` |
| `CustomException` | `StaticErrors.LISTING_NOT_FOUND` | `src/marketplace/marketplace.service.ts:1319` |
| `CustomException` | `StaticErrors.USER_NOT_FOUND` | `src/marketplace/marketplace.service.ts:1333` |
| `CustomException` | `StaticErrors.LISTING_NOT_FOUND` | `src/marketplace/marketplace.service.ts:1515` |
| `CustomException` | `StaticErrors.USER_NOT_FOUND` | `src/marketplace/marketplace.service.ts:1529` |
| `CustomException` | `StaticErrors.OFFER_NOT_FOUND` | `src/marketplace/marketplace.service.ts:1633` |
| `CustomException` | `StaticErrors.UNAUTHORIZED` | `src/marketplace/marketplace.service.ts:1638` |
| `CustomException` | `StaticErrors.INVALID_OFFER_STATUS` | `src/marketplace/marketplace.service.ts:1643` |
| `CustomException` | `StaticErrors.OFFER_COUNTER_LIMIT_REACHED` | `src/marketplace/marketplace.service.ts:1648` |
| `CustomException` | `StaticErrors.OFFER_NOT_FOUND` | `src/marketplace/marketplace.service.ts:1696` |
| `CustomException` | `StaticErrors.UNAUTHORIZED` | `src/marketplace/marketplace.service.ts:1701` |
| `CustomException` | `StaticErrors.INVALID_OFFER_STATUS` | `src/marketplace/marketplace.service.ts:1706` |
| `CustomException` | `StaticErrors.OFFER_EXPIRED` | `src/marketplace/marketplace.service.ts:1711` |
| `CustomException` | `StaticErrors.LISTING_NOT_FOUND` | `src/marketplace/marketplace.service.ts:329` |
| `CustomException` | `StaticErrors.UNAUTHORIZED` | `src/marketplace/marketplace.service.ts:335` |
| `CustomException` | `StaticErrors.LISTING_NOT_FOUND` | `src/marketplace/marketplace.service.ts:351` |
| `CustomException` | `StaticErrors.USER_NOT_FOUND` | `src/marketplace/marketplace.service.ts:374` |
| `CustomException` | `StaticErrors.LISTING_NOT_FOUND` | `src/marketplace/marketplace.service.ts:432` |
| `CustomException` | `StaticErrors.USER_NOT_FOUND` | `src/marketplace/marketplace.service.ts:455` |
| `CustomException` | `StaticErrors.LISTING_NOT_FOUND` | `src/marketplace/marketplace.service.ts:560` |
| `CustomException` | `StaticErrors.USER_NOT_FOUND` | `src/marketplace/marketplace.service.ts:574` |
| `CustomException` | `StaticErrors.LISTING_NOT_FOUND` | `src/marketplace/marketplace.service.ts:641` |
| `CustomException` | `StaticErrors.USER_NOT_FOUND` | `src/marketplace/marketplace.service.ts:649` |
| `CustomException` | `StaticErrors.LISTING_NOT_FOUND` | `src/marketplace/marketplace.service.ts:679` |
| `CustomException` | `StaticErrors.USER_NOT_FOUND` | `src/marketplace/marketplace.service.ts:693` |
| `CustomException` | `StaticErrors.LISTING_NOT_FOUND` | `src/marketplace/marketplace.service.ts:781` |
| `CustomException` | `StaticErrors.WRONG_PAYMENT_METHOD` | `src/marketplace/marketplace.service.ts:784` |
| `CustomException` | `StaticErrors.USER_NOT_FOUND` | `src/marketplace/marketplace.service.ts:789` |
| `CustomException` | `'Transfer is being processed, please try again shortly' as unknown as StaticErrors` | `src/marketplace/marketplace.service.ts:833` |
| `CustomException` | `'Transfer is in an unexpected state. Please contact support.' as unknown as StaticErrors` | `src/marketplace/marketplace.service.ts:904` |
| `CustomException` | `StaticErrors.WRONG_LISTING_STATUS` | `src/marketplace/marketplace.service.ts:909` |
| `CustomException` | `StaticErrors.MIN_PRICE_TWO_DOLLARS` | `src/marketplace/marketplace.service.ts:916` |
| `CustomException` | `StaticErrors.INVALID_PARAMETERS` | `src/marketplace/marketplace.service.ts:923` |
| `CustomException` | `StaticErrors.INVALID_PARAMETERS` | `src/marketplace/marketplace.service.ts:928` |
| `CustomException` | `StaticErrors.LISTING_NOT_FOUND` | `src/marketplace/marketplace.service.ts:933` |
| `CustomException` | `StaticErrors.CANT_CHANGE_LISTING_STATUS` | `src/marketplace/marketplace.service.ts:941` |
| `BadRequestException` | `'Cannot create offers on private listings'` | `src/marketplace/marketplace.service.ts:945` |
| `CustomException` | `StaticErrors.OFFER_EXISTS` | `src/marketplace/marketplace.service.ts:951` |
| `CustomException` | `StaticErrors.NOT_OWNER` | `src/marketplace/marketplace.service.ts:956` |
| `CustomException` | `StaticErrors.OFFER_PROCESSING` | `src/marketplace/marketplace.service.ts:989` |
| `throw` | `err` | `src/mention/mention.service.ts:71` |
| `throw` | `err` | `src/metrics/typeorm-metrics.service.ts:84` |
| `Error` | `'Unexpected FK references to notification_type found.'` | `src/migrations/1774100000000-NotificationMultiSinkSchema.ts:19` |
| `Error` | `'NotificationMultiSinkRenames is not reversible'` | `src/migrations/1774100000001-NotificationMultiSinkRenames.ts:148` |
| `CustomException` | `StaticErrors.LISTING_NOT_FOUND` | `src/moderation/moderation.service.ts:179` |
| `CustomException` | `StaticErrors.ITEM_NOT_FOUND` | `src/moderation/moderation.service.ts:304` |
| `CustomException` | `StaticErrors.ITEM_NOT_FOUND` | `src/moderation/moderation.service.ts:401` |
| `BadRequestException` | `'Agents cannot unlink directly. The operator manages the Telegram link.'` | `src/notifications/controllers/telegram.controller.ts:140` |
| `BadRequestException` | `'Agent has no active operator. Contact admin to assign one before enabling Telegram.'` | `src/notifications/controllers/telegram.controller.ts:79` |
| `throw` | `error` | `src/notifications/handlers/telegram-outbox.handler.ts:83` |
| `CustomException` | `StaticErrors.ITEM_NOT_FOUND` | `src/notifications/notifications.service.ts:227` |
| `throw` | `error` | `src/notifications/providers/sendgrid-email.provider.ts:54` |
| `throw` | `error` | `src/notifications/services/anonymous-email-sender.service.ts:30` |
| `Error` | ``User ${userId} not found`` | `src/notifications/services/notification-dispatcher.service.ts:126` |
| `Error` | `'Redis cache client not available'` | `src/notifications/services/telegram-bot.service.ts:162` |
| `throw` | `err` | `src/notifications/services/telegram-bot.service.ts:170` |
| `Error` | `'Telegram bot not initialized'` | `src/notifications/services/telegram-bot.service.ts:183` |
| `throw` | `err` | `src/notifications/transports/email.transport.ts:41` |
| `throw` | `err` | `src/notifications/transports/in-app.transport.ts:45` |
| `throw` | `err` | `src/notifications/transports/telegram.transport.ts:75` |
| `CustomException` | `StaticErrors.TOKEN_NOT_FOUND` | `src/pay-token/pay-token.service.ts:172` |
| `CustomException` | `StaticErrors.TOKEN_EXISTS` | `src/pay-token/pay-token.service.ts:186` |
| `CustomException` | `StaticErrors.INVALID_PARAMETERS` | `src/pay-token/pay-token.service.ts:191` |
| `CustomException` | `StaticErrors.ITEM_NOT_FOUND` | `src/pay-token/pay-token.service.ts:205` |
| `CustomException` | `StaticErrors.ASSETS_NOT_READY` | `src/pay-token/pay-token.service.ts:208` |
| `CustomException` | `StaticErrors.TOKEN_NOT_FOUND` | `src/pay-token/pay-token.service.ts:250` |
| `CustomException` | `StaticErrors.CANT_REMOVE_TOKEN` | `src/pay-token/pay-token.service.ts:266` |
| `CustomException` | `StaticErrors.TOKEN_NOT_FOUND` | `src/pay-token/pay-token.service.ts:278` |
| `CustomException` | `StaticErrors.INVALID_PARAMETERS` | `src/pay-token/pay-token.service.ts:371` |
| `Error` | ``PayPal capture failed for auth ${authorizationId}`` | `src/paypal/paypal-outbox.handlers.ts:176` |
| `throw` | `err` | `src/paypal/paypal-outbox.handlers.ts:245` |
| `Error` | ``Buyer ${buyerId} has no wallet address`` | `src/paypal/paypal-outbox.handlers.ts:292` |
| `Error` | ``buyItemBC failed for listing ${listingId}, contract ${listingContractId}, tx ${transactionId}`` | `src/paypal/paypal-outbox.handlers.ts:298` |
| `Error` | ``acceptOfferBC failed for listing ${listingId}: ${JSON.stringify(result.error)}`` | `src/paypal/paypal-outbox.handlers.ts:382` |
| `NonRetryableError` | ``PayPal charge permanently failed: ${issue}` \| { issue, transactionId: payload.transactionId }` | `src/paypal/paypal-outbox.handlers.ts:74` |
| `throw` | `error` | `src/paypal/paypal-outbox.handlers.ts:79` |
| `Error` | ``PayPal charge status: ${status}`` | `src/paypal/paypal-outbox.handlers.ts:83` |
| `CustomException` | `StaticErrors.PRICE_TOO_LOW_FOR_FEES \| HttpStatus.UNPROCESSABLE_ENTITY` | `src/paypal/paypal.service.ts:1062` |
| `CustomException` | `StaticErrors.MIN_PRICE_TWO_DOLLARS` | `src/paypal/paypal.service.ts:1284` |
| `CustomException` | `StaticErrors.OFFER_PROCESSING` | `src/paypal/paypal.service.ts:1296` |
| `CustomException` | `StaticErrors.LISTING_NOT_FOUND` | `src/paypal/paypal.service.ts:1305` |
| `CustomException` | `StaticErrors.WRONG_PAYMENT_METHOD` | `src/paypal/paypal.service.ts:1309` |
| `CustomException` | `StaticErrors.USER_NOT_FOUND` | `src/paypal/paypal.service.ts:1318` |
| `CustomException` | `message as unknown as StaticErrors` | `src/paypal/paypal.service.ts:1326` |
| `CustomException` | `StaticErrors.BUYER_NOT_ONBOARDED` | `src/paypal/paypal.service.ts:1330` |
| `CustomException` | `StaticErrors.LISTING_NOT_FOUND` | `src/paypal/paypal.service.ts:1366` |
| `CustomException` | `StaticErrors.WRONG_PAYMENT_METHOD` | `src/paypal/paypal.service.ts:1370` |
| `CustomException` | `StaticErrors.LISTING_NOT_FOR_SALE` | `src/paypal/paypal.service.ts:1374` |
| `CustomException` | `StaticErrors.USER_NOT_FOUND` | `src/paypal/paypal.service.ts:1383` |
| `CustomException` | `message as unknown as StaticErrors` | `src/paypal/paypal.service.ts:1391` |
| `CustomException` | `StaticErrors.BUYER_NOT_ONBOARDED` | `src/paypal/paypal.service.ts:1395` |
| `CustomException` | `StaticErrors.WRONG_LISTING_STATUS` | `src/paypal/paypal.service.ts:1399` |
| `CustomException` | `StaticErrors.LISTING_NOT_FOUND` | `src/paypal/paypal.service.ts:1440` |
| `CustomException` | `StaticErrors.WRONG_PAYMENT_METHOD` | `src/paypal/paypal.service.ts:1443` |
| `CustomException` | `StaticErrors.LISTING_NOT_FOR_SALE` | `src/paypal/paypal.service.ts:1446` |
| `CustomException` | `StaticErrors.WRONG_LISTING_STATUS` | `src/paypal/paypal.service.ts:1452` |
| `CustomException` | `StaticErrors.CANT_BUY_OWN_LISTING` | `src/paypal/paypal.service.ts:1455` |
| `CustomException` | `StaticErrors.USER_NOT_FOUND` | `src/paypal/paypal.service.ts:1464` |
| `CustomException` | `message as unknown as StaticErrors` | `src/paypal/paypal.service.ts:1471` |
| `CustomException` | `StaticErrors.BUYER_NOT_ONBOARDED` | `src/paypal/paypal.service.ts:1474` |
| `CustomException` | `StaticErrors.LISTING_NOT_FOUND` | `src/paypal/paypal.service.ts:1548` |
| `CustomException` | `StaticErrors.LISTING_NOT_FOR_SALE` | `src/paypal/paypal.service.ts:1552` |
| `CustomException` | `StaticErrors.ALREADY_HAS_DOWNLOAD_LICENSE` | `src/paypal/paypal.service.ts:1561` |
| `CustomException` | `StaticErrors.USER_NOT_FOUND` | `src/paypal/paypal.service.ts:1572` |
| `CustomException` | `message as unknown as StaticErrors` | `src/paypal/paypal.service.ts:1580` |
| `CustomException` | `StaticErrors.SESSION_NOT_FOUND` | `src/paypal/paypal.service.ts:1619` |
| `CustomException` | `StaticErrors.PAYPAL_BILLING_SETUP_FAILED` | `src/paypal/paypal.service.ts:1673` |
| `CustomException` | `StaticErrors.PAYPAL_BILLING_SETUP_FAILED` | `src/paypal/paypal.service.ts:1685` |
| `CustomException` | `StaticErrors.PAYPAL_PAYMENT_TOKEN_FAILED` | `src/paypal/paypal.service.ts:1721` |
| `CustomException` | `'PayPal service unavailable' as StaticErrors` | `src/paypal/paypal.service.ts:173` |
| `CustomException` | `StaticErrors.PRICE_TOO_LOW_FOR_FEES \| HttpStatus.UNPROCESSABLE_ENTITY` | `src/paypal/paypal.service.ts:1789` |
| `throw` | `wrapped` | `src/paypal/paypal.service.ts:1867` |
| `Error` | `'No authorization ID in PayPal response'` | `src/paypal/paypal.service.ts:1921` |
| `CustomException` | `StaticErrors.SESSION_NOT_FOUND` | `src/paypal/paypal.service.ts:1940` |
| `CustomException` | `StaticErrors.LISTING_NOT_FOUND` | `src/paypal/paypal.service.ts:1964` |
| `CustomException` | `StaticErrors.WRONG_LISTING_STATUS` | `src/paypal/paypal.service.ts:1967` |
| `throw` | `err` | `src/paypal/paypal.service.ts:2037` |
| `CustomException` | `StaticErrors.USER_NOT_FOUND` | `src/paypal/paypal.service.ts:261` |
| `CustomException` | `StaticErrors.KYC_ALREADY_DONE` | `src/paypal/paypal.service.ts:265` |
| `CustomException` | `StaticErrors.USER_NOT_FOUND` | `src/paypal/paypal.service.ts:314` |
| `CustomException` | `StaticErrors.USER_NOT_FOUND` | `src/paypal/paypal.service.ts:413` |
| `CustomException` | `StaticErrors.USER_NOT_FOUND` | `src/paypal/paypal.service.ts:536` |
| `CustomException` | `StaticErrors.USER_NOT_FOUND` | `src/paypal/paypal.service.ts:579` |
| `CustomException` | `StaticErrors.PRICE_TOO_LOW_FOR_FEES \| HttpStatus.UNPROCESSABLE_ENTITY` | `src/paypal/paypal.service.ts:885` |
| `CustomException` | `StaticErrors.REWARD_TYPE_ALREADY_EXISTS` | `src/point/point.service.ts:133` |
| `CustomException` | `StaticErrors.REWARD_TYPE_NOT_FOUND` | `src/point/point.service.ts:157` |
| `throw` | `error` | `src/rate-limit/user-rate-limit.interceptor.ts:104` |
| `HttpException` | `{ statusCode: HttpStatus.TOO_MANY_REQUESTS, message: 'Rate limit exceeded.', error: 'RATE_LIMITED', retryAfter, } \| HttpStatus.TOO_MANY_REQUESTS` | `src/rate-limit/user-rate-limit.interceptor.ts:92` |
| `Error` | ``Redis connection failed after ${maxRetries} attempts: ${errorMessage}`` | `src/redis/redis.service.ts:129` |
| `Error` | ``Outbox handler already registered for: ${eventType}`` | `src/resilience/outbox/outbox.service.ts:50` |
| `Error` | ``Dead-letter handler already registered for: ${eventType}`` | `src/resilience/outbox/outbox.service.ts:64` |
| `throw` | `error` | `src/resilience/retry/with-retry.ts:53` |
| `throw` | `lastError` | `src/resilience/retry/with-retry.ts:72` |
| `throw` | `err` | `src/search/search-outbox.handler.ts:68` |
| `throw` | `error` | `src/search/typesense.service.ts:248` |
| `throw` | `error` | `src/search/typesense.service.ts:302` |
| `Error` | ``Typesense partial upsert failure in ${collectionName}: ${failedIds.length}/${documents.length} documents failed (ids: ${failedIds.slice(0, 5).join(', ')})`` | `src/search/typesense.service.ts:317` |
| `throw` | `error` | `src/search/typesense.service.ts:361` |
| `throw` | `error` | `src/search/typesense.service.ts:393` |
| `throw` | `error` | `src/search/typesense.service.ts:411` |
| `throw` | `error` | `src/search/typesense.service.ts:576` |
| `CustomException` | `StaticErrors.USER_NOT_FOUND` | `src/transaction/transaction.service.ts:30` |
| `CustomException` | `StaticErrors.LISTING_NOT_FOUND` | `src/transaction/transaction.service.ts:40` |
| `CustomException` | `StaticErrors.EXIST_TRANSACTION` | `src/transaction/transaction.service.ts:49` |
| `BadRequestException` | `'Queue is full — remove an entry before adding more.'` | `src/user-feed-queue/services/user-feed-queue.service.ts:118` |
| `ForbiddenException` | `'Queue entry not found or not yours'` | `src/user-feed-queue/services/user-feed-queue.service.ts:267` |
| `NotFoundException` | `'Queue entry not found'` | `src/user-feed-queue/services/user-feed-queue.service.ts:283` |
| `ForbiddenException` | `'Cannot reorder the current or played entries.'` | `src/user-feed-queue/services/user-feed-queue.service.ts:288` |
| `ForbiddenException` | `'Cannot reorder the current or played entries.'` | `src/user-feed-queue/services/user-feed-queue.service.ts:299` |
| `BadRequestException` | `'afterEntryId not found'` | `src/user-feed-queue/services/user-feed-queue.service.ts:316` |
| `BadRequestException` | `'beforeEntryId not found'` | `src/user-feed-queue/services/user-feed-queue.service.ts:319` |
| `ForbiddenException` | `'Cannot anchor reorder on the current entry.'` | `src/user-feed-queue/services/user-feed-queue.service.ts:328` |
| `ForbiddenException` | `'afterEntryId is at or after the current entry — played entries are immutable.'` | `src/user-feed-queue/services/user-feed-queue.service.ts:334` |
| `ForbiddenException` | `'beforeEntryId is at or after the current entry — played entries are immutable.'` | `src/user-feed-queue/services/user-feed-queue.service.ts:339` |
| `ForbiddenException` | `'Computed rank would cross the active boundary.'` | `src/user-feed-queue/services/user-feed-queue.service.ts:351` |
| `BadRequestException` | `'Invalid cursor'` | `src/user-feed-queue/services/user-feed-queue.service.ts:42` |
| `NotFoundException` | `'Folder not found'` | `src/user-feed-queue/services/user-feed-queue.service.ts:431` |
| `ForbiddenException` | `'This folder is not available to add.'` | `src/user-feed-queue/services/user-feed-queue.service.ts:435` |
| `NotFoundException` | `'Asset not found'` | `src/user-feed-queue/services/user-feed-queue.service.ts:442` |
| `ForbiddenException` | `'This asset is not available to add.'` | `src/user-feed-queue/services/user-feed-queue.service.ts:448` |
| `BadRequestException` | `'Unknown target type'` | `src/user-feed-queue/services/user-feed-queue.service.ts:451` |
| `BadRequestException` | `'Invalid cursor'` | `src/user-feed-queue/services/user-feed-queue.service.ts:46` |
| `BadRequestException` | `'Invalid cursor'` | `src/user-feed-queue/services/user-feed-queue.service.ts:51` |
| `Error` | `'preloadedEntry.userId does not match userId'` | `src/user-feed-queue/services/user-feed-queue.service.ts:515` |
| `Error` | `'preloadedEntry.id does not match entryId'` | `src/user-feed-queue/services/user-feed-queue.service.ts:518` |
| `BadRequestException` | `'Invalid cursor'` | `src/user-feed-queue/services/user-feed-queue.service.ts:54` |
| `Error` | ``profile-counts cache: invalid userId shape "${targetUserId}" — expected UUID`` | `src/user/profile-counts.cache.ts:148` |
| `Error` | ``profile-counts cache: invalid userId shape "${targetUserId}" — expected UUID`` | `src/user/profile-counts.cache.ts:157` |
| `CustomException` | `StaticErrors.USER_NOT_FOUND` | `src/user/user.query.ts:161` |
| `CustomException` | `StaticErrors.ITEM_NOT_FOUND` | `src/user/user.query.ts:252` |
| `CustomException` | `StaticErrors.USER_NOT_FOUND` | `src/user/user.query.ts:48` |
| `CustomException` | `StaticErrors.USER_NOT_FOUND` | `src/user/user.query.ts:60` |
| `CustomException` | `StaticErrors.USER_NOT_FOUND` | `src/user/user.query.ts:84` |
| `CustomException` | `StaticErrors.WRONG_2FA_CODE` | `src/user/user.service.ts:1027` |
| `throw` | `error` | `src/user/user.service.ts:1029` |
| `CustomException` | `StaticErrors.WRONG_2FA_CODE` | `src/user/user.service.ts:1036` |
| `CustomException` | `StaticErrors.EMAIL_NOT_CONFIRMED` | `src/user/user.service.ts:1056` |
| `CustomException` | `StaticErrors.USER_NOT_FOUND` | `src/user/user.service.ts:1091` |
| `CustomException` | `StaticErrors.INVALID_USER_PASS` | `src/user/user.service.ts:1096` |
| `CustomException` | `StaticErrors.EMAIL_NOT_CONFIRMED` | `src/user/user.service.ts:1101` |
| `CustomException` | `StaticErrors.USER_2FA_REQUIRED` | `src/user/user.service.ts:1106` |
| `CustomException` | `StaticErrors.INVALID_USER_PASS` | `src/user/user.service.ts:1121` |
| `throw` | `error` | `src/user/user.service.ts:1124` |
| `CustomException` | `StaticErrors.USER_2FA_REQUIRED` | `src/user/user.service.ts:1133` |
| `CustomException` | `StaticErrors.WRONG_2FA_CODE` | `src/user/user.service.ts:1148` |
| `throw` | `error` | `src/user/user.service.ts:1150` |
| `CustomException` | `StaticErrors.WRONG_2FA_CODE` | `src/user/user.service.ts:1157` |
| `CustomException` | `StaticErrors.EMAIL_ALREADY_IN_WAITLIST` | `src/user/user.service.ts:1210` |
| `CustomException` | `StaticErrors.USER_NOT_FOUND` | `src/user/user.service.ts:1234` |
| `CustomException` | `StaticErrors.ITEM_NOT_FOUND` | `src/user/user.service.ts:1291` |
| `CustomException` | `StaticErrors.ITEM_NOT_FOUND` | `src/user/user.service.ts:1311` |
| `CustomException` | `StaticErrors.USER_NOT_FOUND` | `src/user/user.service.ts:1332` |
| `Error` | `'Failed to create registration token'` | `src/user/user.service.ts:1378` |
| `CustomException` | `StaticErrors.USER_NOT_FOUND` | `src/user/user.service.ts:1401` |
| `CustomException` | `StaticErrors.USER_NOT_FOUND` | `src/user/user.service.ts:1417` |
| `CustomException` | `StaticErrors.PASSWORD_RESET_LINK_EXPIRED` | `src/user/user.service.ts:1431` |
| `throw` | `error` | `src/user/user.service.ts:1433` |
| `CustomException` | `StaticErrors.INVALID_USER_PASS` | `src/user/user.service.ts:1457` |
| `throw` | `error` | `src/user/user.service.ts:1460` |
| `CustomException` | `StaticErrors.EMAIL_VERIFICATION_FAILED` | `src/user/user.service.ts:1497` |
| `CustomException` | `StaticErrors.EMAIL_VERIFICATION_FAILED` | `src/user/user.service.ts:1504` |
| `CustomException` | `StaticErrors.EMAIL_VERIFICATION_FAILED` | `src/user/user.service.ts:1522` |
| `throw` | `error` | `src/user/user.service.ts:1524` |
| `CustomException` | `StaticErrors.USER_NOT_FOUND` | `src/user/user.service.ts:1602` |
| `CustomException` | `StaticErrors.EMAIL_ALREADY_CONFIRMED` | `src/user/user.service.ts:1605` |
| `CustomException` | `StaticErrors.EMAIL_VERIFICATION_FAILED` | `src/user/user.service.ts:1619` |
| `CustomException` | `StaticErrors.USER_NOT_FOUND` | `src/user/user.service.ts:1627` |
| `CustomException` | `StaticErrors.USER_NOT_FOUND` | `src/user/user.service.ts:1646` |
| `CustomException` | `StaticErrors.USER_NOT_FOUND` | `src/user/user.service.ts:1663` |
| `CustomException` | `StaticErrors.USER_NOT_FOUND` | `src/user/user.service.ts:1679` |
| `CustomException` | `StaticErrors.USER_NOT_FOUND` | `src/user/user.service.ts:1694` |
| `CustomException` | `StaticErrors.USER_NOT_FOUND` | `src/user/user.service.ts:1709` |
| `CustomException` | `StaticErrors.WRONG_BIO_LENGTH` | `src/user/user.service.ts:1713` |
| `CustomException` | `StaticErrors.USER_NOT_FOUND` | `src/user/user.service.ts:1755` |
| `CustomException` | `StaticErrors.USER_NAME_ALREADY_SET` | `src/user/user.service.ts:1759` |
| `CustomException` | `StaticErrors.USER_NOT_FOUND` | `src/user/user.service.ts:1780` |
| `CustomException` | `StaticErrors.ITEM_NOT_FOUND` | `src/user/user.service.ts:1884` |
| `CustomException` | `StaticErrors.USER_NOT_FOUND` | `src/user/user.service.ts:1922` |
| `CustomException` | `StaticErrors.USER_NOT_FOUND` | `src/user/user.service.ts:1969` |
| `BadRequestException` | ``Invalid roleId ${input.roleId}. Expected one of: ${Object.values(USER_ROLES).join(', ')}`` | `src/user/user.service.ts:2016` |
| `CustomException` | `StaticErrors.USER_NOT_FOUND` | `src/user/user.service.ts:2024` |
| `CustomException` | `StaticErrors.USER_NOT_FOUND` | `src/user/user.service.ts:2043` |
| `CustomException` | `StaticErrors.USER_2FA_ALREADY_CONFIRMED` | `src/user/user.service.ts:2047` |
| `CustomException` | `StaticErrors.WRONG_PASSWORD` | `src/user/user.service.ts:2067` |
| `throw` | `error` | `src/user/user.service.ts:2070` |
| `CustomException` | `StaticErrors.USER_NOT_FOUND` | `src/user/user.service.ts:2091` |
| `CustomException` | `StaticErrors.WRONG_2FA_CODE` | `src/user/user.service.ts:2108` |
| `throw` | `error` | `src/user/user.service.ts:2110` |
| `CustomException` | `StaticErrors.WRONG_2FA_CODE` | `src/user/user.service.ts:2129` |
| `CustomException` | `StaticErrors.WRONG_2FA_CODE` | `src/user/user.service.ts:2137` |
| `CustomException` | `StaticErrors.USER_NOT_FOUND` | `src/user/user.service.ts:2145` |
| `CustomException` | `StaticErrors.WALLET_NOT_FOUND` | `src/user/user.service.ts:2235` |
| `CustomException` | `StaticErrors.WALLET_ALREADY_TAKEN` | `src/user/user.service.ts:2239` |
| `CustomException` | `StaticErrors.USER_NOT_FOUND` | `src/user/user.service.ts:2263` |
| `CustomException` | `StaticErrors.ITEM_NOT_FOUND` | `src/user/user.service.ts:2311` |
| `CustomException` | `StaticErrors.ITEM_NOT_FOUND` | `src/user/user.service.ts:2329` |
| `CustomException` | `StaticErrors.ITEM_NOT_FOUND` | `src/user/user.service.ts:2356` |
| `CustomException` | `StaticErrors.ITEM_NOT_FOUND` | `src/user/user.service.ts:2373` |
| `CustomException` | `StaticErrors.USER_NOT_FOUND` | `src/user/user.service.ts:2504` |
| `CustomException` | `StaticErrors.USER_NOT_FOUND` | `src/user/user.service.ts:2522` |
| `CustomException` | `StaticErrors.INVALID_REFERRAL_CODE` | `src/user/user.service.ts:334` |
| `CustomException` | `StaticErrors.INVALID_REFERRAL_CODE` | `src/user/user.service.ts:378` |
| `CustomException` | `StaticErrors.INVALID_INVITE_CODE` | `src/user/user.service.ts:387` |
| `CustomException` | `StaticErrors.INVALID_INVITE_CODE` | `src/user/user.service.ts:393` |
| `CustomException` | `StaticErrors.REGISTRATION_TOKEN_EXPIRED` | `src/user/user.service.ts:396` |
| `CustomException` | `StaticErrors.REGISTRATION_TOKEN_EXPIRED` | `src/user/user.service.ts:402` |
| `CustomException` | `StaticErrors.USER_NOT_FOUND` | `src/user/user.service.ts:452` |
| `CustomException` | `StaticErrors.USER_NOT_FOUND` | `src/user/user.service.ts:467` |
| `CustomException` | `StaticErrors.USER_NOT_FOUND` | `src/user/user.service.ts:507` |
| `CustomException` | `StaticErrors.WRONG_USER_NAME` | `src/user/user.service.ts:726` |
| `CustomException` | `StaticErrors.USER_NAME_TAKEN` | `src/user/user.service.ts:730` |
| `CustomException` | `StaticErrors.USER_NAME_TAKEN` | `src/user/user.service.ts:738` |
| `CustomException` | `errorMessage as StaticErrors` | `src/user/user.service.ts:770` |
| `CustomException` | `StaticErrors.EMAIL_REGISTERED` | `src/user/user.service.ts:793` |
| `throw` | `error` | `src/user/user.service.ts:795` |
| `throw` | `error` | `src/user/user.service.ts:899` |
| `CustomException` | `StaticErrors.USER_NOT_FOUND` | `src/user/user.service.ts:907` |
| `CustomException` | `StaticErrors.INVITE_SAME_USER` | `src/user/user.service.ts:911` |
| `CustomException` | `StaticErrors.INVITE_REGISTERED_EMAIL` | `src/user/user.service.ts:917` |
| `CustomException` | `StaticErrors.REGISTRATION_TOKEN_EXPIRED` | `src/user/user.service.ts:933` |
| `CustomException` | `StaticErrors.INVITE_LIMIT_REACHED` | `src/user/user.service.ts:938` |
| `CustomException` | `StaticErrors.INVALID_EMAIL` | `src/user/user.service.ts:971` |
| `CustomException` | `StaticErrors.WRONG_PASSWORD` | `src/user/user.service.ts:991` |
| `throw` | `error` | `src/user/user.service.ts:994` |
| `CustomException` | `StaticErrors.INVALID_REFERRAL_CODE` | `src/user/utils/referral.ts:14` |
| `CustomException` | `StaticErrors.INVALID_URL` | `src/utils/generalHelper.ts:276` |
| `CustomException` | `StaticErrors.INVALID_URL` | `src/utils/generalHelper.ts:280` |
| `CustomException` | `StaticErrors.INVALID_URL` | `src/utils/generalHelper.ts:288` |
| `CustomException` | `StaticErrors.INVALID_URL` | `src/utils/generalHelper.ts:293` |
| `Error` | ``Unsupported period unit: ${unit}`` | `src/utils/generalHelper.ts:337` |
| `GraphQLError` | `'Invalid API key' \| { extensions: { code: 'UNAUTHENTICATED', status: 401 }, }` | `src/utils/gqlAuth.guard.ts:110` |
| `GraphQLError` | `'Agent account is deactivated' \| { extensions: { code: 'UNAUTHENTICATED', status: 401 }, }` | `src/utils/gqlAuth.guard.ts:115` |
| `GraphQLError` | `'Agents must use the REST API at /api/v1/agents/*' \| { extensions: { code: 'FORBIDDEN', status: 403 }, }` | `src/utils/gqlAuth.guard.ts:123` |
| `throw` | `err` | `src/utils/gqlAuth.guard.ts:131` |
| `GraphQLError` | `'Rate limit exceeded' \| { extensions: { code: 'RATE_LIMITED', status: 429 }, }` | `src/utils/gqlAuth.guard.ts:135` |
| `GraphQLError` | `'Invalid API key' \| { extensions: { code: 'UNAUTHENTICATED', status: 401 }, }` | `src/utils/gqlAuth.guard.ts:140` |
| `UnauthorizedException` | `` | `src/utils/gqlAuth.guard.ts:178` |
| `GraphQLError` | `'Agents must use the REST API at /api/v1/agents/*' \| { extensions: { code: 'FORBIDDEN', status: 403 } }` | `src/utils/gqlAuth.guard.ts:37` |
| `GraphQLError` | `'Rate limit exceeded' \| { extensions: { code: 'RATE_LIMITED', status: 429 }, }` | `src/utils/gqlAuth.guard.ts:87` |
| `GraphQLError` | `'Invalid API key' \| { extensions: { code: 'UNAUTHENTICATED', status: 401 }, }` | `src/utils/gqlAuth.guard.ts:92` |
| `HttpException` | `{ statusCode: HttpStatus.TOO_MANY_REQUESTS, message: 'Too many requests, please try again later.', error: 'RATE_LIMITED', retryAfter, } \| HttpStatus.TOO_MANY_REQUESTS` | `src/utils/gqlThrottler.guard.ts:32` |
| `NotFoundException` | `{ statusCode: 404, message: 'Not Found', code: 'MARKETPLACE_DISABLED', }` | `src/utils/marketplace-enabled.guard.ts:42` |
| `NotFoundException` | `` | `src/utils/marketplace-enabled.guard.ts:53` |
| `NotFoundException` | `{ statusCode: 404, error: 'NOT_FOUND', code: 'MARKETPLACE_DISABLED', message: 'Marketplace is not available at this time', hint: 'Commerce endpoints are hidden at launch; see skills/reference.md#marketplace-fields.', }` | `src/utils/marketplace-enabled.guard.ts:57` |
| `throw` | `error` | `src/viral-score/folder-viral-score.processor.ts:110` |
| `throw` | `error` | `src/viral-score/folder-viral-score.processor.ts:32` |
| `throw` | `error` | `src/viral-score/folder-viral-score.processor.ts:49` |
| `throw` | `error` | `src/viral-score/folder-viral-score.processor.ts:66` |
| `throw` | `error` | `src/viral-score/folder-viral-score.processor.ts:95` |
| `throw` | `queueErr` | `src/viral-score/folder-viral-score.service.ts:116` |
| `throw` | `error` | `src/viral-score/folder-viral-score.service.ts:171` |
| `throw` | `error` | `src/viral-score/folder-viral-score.service.ts:245` |
| `throw` | `error` | `src/viral-score/folder-viral-score.service.ts:426` |
| `throw` | `error` | `src/viral-score/folder-viral-score.service.ts:557` |
| `throw` | `error` | `src/viral-score/viral-score.processor.ts:22` |
| `throw` | `error` | `src/viral-score/viral-score.processor.ts:34` |
| `throw` | `error` | `src/viral-score/viral-score.processor.ts:46` |
| `throw` | `error` | `src/viral-score/viral-score.processor.ts:74` |
| `throw` | `error` | `src/viral-score/viral-score.processor.ts:87` |
| `throw` | `error` | `src/viral-score/viral-score.service.ts:1052` |
| `throw` | `error` | `src/viral-score/viral-score.service.ts:147` |
| `throw` | `error` | `src/viral-score/viral-score.service.ts:272` |
| `throw` | `error` | `src/viral-score/viral-score.service.ts:852` |
| `throw` | `error` | `src/viral-score/viral-score.service.ts:954` |
| `NonRetryableError` | ``Webhook delivery permanently failed: ${(error as Error).message}` \| { endpointId, endpointUrl, status, code }` | `src/webhook/webhook-outbox.handler.ts:142` |
| `throw` | `error` | `src/webhook/webhook-outbox.handler.ts:148` |
| `NonRetryableError` | `'Webhook delivery permanently failed: SSRF blocked' \| { endpointId, endpointUrl, code: 'SSRF_BLOCKED', }` | `src/webhook/webhook-outbox.handler.ts:95` |
| `NotFoundException` | `'Webhook endpoint not found'` | `src/webhook/webhook.controller.ts:55` |
| `NotFoundException` | `'Webhook endpoint not found'` | `src/webhook/webhook.controller.ts:68` |
| `NotFoundException` | `'Webhook endpoint not found'` | `src/webhook/webhook.controller.ts:76` |
| `throw` | `err` | `src/webhook/webhook.service.ts:152` |
| `BadRequestException` | ``Maximum ${maxEndpoints} webhook endpoints per user`` | `src/webhook/webhook.service.ts:42` |
| `throw` | `err` | `src/webhook/webhook.service.ts:60` |
