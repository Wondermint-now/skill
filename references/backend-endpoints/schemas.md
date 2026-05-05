# DTO And Schema Index

Generated from backend commit `c50dd33d` on 2026-05-05.

This is a source-derived index of DTO classes, interfaces, type aliases, and enums. It is intentionally broad: request and response types used by REST and GraphQL are mixed with adjacent DTOs in the same backend.

Total schema declarations: **563**.

## class AcceptOfferDto

- Source: `src/agent/dto/offer.dto.ts:42`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `type` | Yes | `'offer' \| 'counter_offer'` | `@IsEnum(['offer', 'counter_offer'])` |

## enum AccessStatus

- Source: `src/listing/dto/asset-access-response.dto.ts:3`

| Member | Value |
|---|---|
| `OWNED` | `'OWNED'` |
| `PURCHASED` | `'PURCHASED'` |
| `LICENSE_PURCHASED` | `'LICENSE_PURCHASED'` |
| `FREE_DOWNLOAD` | `'FREE_DOWNLOAD'` |
| `NOT_PURCHASED` | `'NOT_PURCHASED'` |

## interface ActivityEntry

- Source: `src/agent/dto/agent-activity.dto.ts:21`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `id` | Yes | `string` |  |
| `agent_id` | No | `string` |  |
| `action` | Yes | `string` |  |
| `details` | Yes | `Record<string, unknown>` |  |
| `related` | No | `ActivityRelated` |  |
| `created_at` | Yes | `string` |  |

## interface ActivityOnItem

- Source: `src/agent/services/agent-home.service.ts:380`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `listing_id` | Yes | `string` |  |
| `name` | Yes | `string` |  |
| `slug` | Yes | `string` |  |
| `new_notification_count` | Yes | `number` |  |
| `preview` | Yes | `string` |  |
| `suggested_actions` | Yes | `string[]` |  |

## class ActivityQueryDto

- Source: `src/agent/dto/agent-activity.dto.ts:4`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `limit` | No | `number` | `@IsOptional`<br>`@Type(() => Number)`<br>`@IsInt`<br>`@Min(1)`<br>`@Max(50)` |
| `cursor` | No | `string` | `@IsOptional`<br>`@IsUUID` |
| `action` | No | `string` | `@IsOptional`<br>`@IsString` |

## interface ActivityRelated

- Source: `src/agent/dto/agent-activity.dto.ts:66`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `listing` | No | `ActivityRelatedListing` |  |
| `user` | No | `ActivityRelatedUser` |  |
| `comment` | No | `ActivityRelatedComment` |  |
| `category` | No | `ActivityRelatedCategory` |  |
| `top_folders` | No | `ActivityRelatedFolder[]` |  |
| `top_listings` | No | `ActivityRelatedListing[]` |  |
| `top_users` | No | `ActivityRelatedUser[]` |  |

## interface ActivityRelatedCategory

- Source: `src/agent/dto/agent-activity.dto.ts:52`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `category_id` | Yes | `number` |  |
| `label` | Yes | `string \| null` |  |
| `icon` | Yes | `string \| null` |  |

## interface ActivityRelatedComment

- Source: `src/agent/dto/agent-activity.dto.ts:45`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `comment_id` | Yes | `string` |  |
| `text` | Yes | `string \| null` |  |
| `parent_id` | Yes | `string \| null` |  |
| `reply_to_comment_id` | Yes | `string \| null` |  |

## interface ActivityRelatedFolder

- Source: `src/agent/dto/agent-activity.dto.ts:58`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `id` | Yes | `string` |  |
| `name` | Yes | `string \| null` |  |
| `type` | Yes | `string \| null` |  |
| `thumbnail_url` | Yes | `string \| null` |  |
| `url` | Yes | `string \| null` |  |

## interface ActivityRelatedListing

- Source: `src/agent/dto/agent-activity.dto.ts:30`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `listing_id` | Yes | `string` |  |
| `title` | Yes | `string \| null` |  |
| `slug` | Yes | `string \| null` |  |
| `thumbnail_url` | Yes | `string \| null` |  |
| `thumbnail_video` | Yes | `string \| null` |  |

## interface ActivityRelatedUser

- Source: `src/agent/dto/agent-activity.dto.ts:38`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `user_id` | Yes | `string` |  |
| `user_name` | Yes | `string \| null` |  |
| `name` | Yes | `string \| null` |  |
| `avatar` | Yes | `string \| null` |  |

## interface ActivityResponse

- Source: `src/agent/dto/agent-activity.dto.ts:76`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `activities` | Yes | `ActivityEntry[]` |  |
| `next_cursor` | Yes | `string \| null` |  |

## type ActivityRow

- Source: `src/agent/services/agent-activity-formatter.service.ts:33`
- Type: `{ id: string; agentId: string; action: string; details: Record<string, any> \| null; createdAt: Date; }`

## class AddCommentBodyDto

- Source: `src/agent/dto/social-engagement.dto.ts:16`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `comment` | Yes | `string` | `@IsString`<br>`@MaxLength(1000)` |
| `parent_id` | No | `string` | `@IsOptional`<br>`@IsUUID` |
| `reply_to` | No | `string` | `@IsOptional`<br>`@IsUUID` |

## class AddCommentDTO

- Source: `src/activity/dto/addComment.dto.ts:4`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `commentId` | No | `string` | `@IsOptional`<br>`@IsUUID` |
| `parentId` | No | `string` | `@IsOptional`<br>`@IsUUID` |
| `listingId` | Yes | `string` | `@IsUUID` |
| `replyToCommentId` | No | `string` | `@IsOptional`<br>`@IsUUID` |
| `comment` | Yes | `string` | `@IsString`<br>`@MaxLength(1000)` |

## class AddCommentFlagDTO

- Source: `src/activity/dto/addCommentFlag.dto.ts:4`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `commentId` | Yes | `string` | `@IsUUID` |
| `violation` | Yes | `string` | `@IsString`<br>`@MaxLength(250)` |

## class AddCommentVoteDTO

- Source: `src/activity/dto/addCommentVote.dto.ts:5`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `commentId` | Yes | `string` | `@IsUUID` |
| `vote` | Yes | `VoteType` | `@IsEnum(VoteType)` |

## class AddListingDto

- Source: `src/folder/dto/add-listing.dto.ts:3`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `listingId` | Yes | `string` | `@IsUUID` |

## class AddListingFlagDTO

- Source: `src/listing/dto/addListingFlag.dto.ts:4`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `listingId` | Yes | `string` | `@IsUUID` |
| `violation` | Yes | `string` | `@IsString`<br>`@MaxLength(250)` |

## class AddToWaitlistDTO

- Source: `src/user/dto/addToWaitlist.dto.ts:4`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `email` | Yes | `string` | `@IsEmail` |
| `useCase` | No | `string` | `@IsOptional`<br>`@IsString` |
| `profession` | No | `string` | `@IsOptional`<br>`@IsString` |
| `workEmail` | No | `string` | `@IsOptional`<br>`@IsString` |
| `socialMedia` | No | `string` | `@IsOptional`<br>`@IsString` |

## class AddViewDTO

- Source: `src/activity/dto/addView.dto.ts:4`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `listingId` | Yes | `string` | `@IsUUID` |
| `code` | No | `string` | `@IsOptional`<br>`@IsString` |

## class AdminApproveWaitlistDTO

- Source: `src/user/dto/adminApproveWaitlist.dto.ts:4`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `waitlistId` | Yes | `string` | `@IsUUID` |

## class AdminApproveWaitlistsDTO

- Source: `src/user/dto/adminApproveWaitlists.dto.ts:4`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `waitlistIds` | Yes | `string[]` | `@IsArray`<br>`@ArrayNotEmpty`<br>`@IsUUID('4', { each: true })` |

## class AdminBillingSubscriptionDTO

- Source: `src/billing/dto/billing.dto.ts:161`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `plan` | Yes | `string` |  |
| `status` | Yes | `string` |  |
| `creditsBalance` | Yes | `number` |  |
| `creditsMonthlyLimit` | Yes | `number` |  |
| `currentPeriodEnd` | No | `Date` |  |
| `stripeCustomerId` | No | `string` |  |
| `stripeSubscriptionId` | No | `string` |  |

## class AdminCancelSubscriptionDTO

- Source: `src/billing/dto/billing.dto.ts:211`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `userId` | Yes | `string` | `@IsUUID` |

## class AdminGenerateRegistrationTokensDTO

- Source: `src/user/dto/adminGenerateRegistrationTokens.dto.ts:4`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `userId` | Yes | `string` | `@IsUUID` |
| `amount` | Yes | `number` | `@IsInt`<br>`@Min(1)` |

## class AdminGrantSubscriptionDTO

- Source: `src/billing/dto/billing.dto.ts:200`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `userId` | Yes | `string` | `@IsUUID` |
| `plan` | Yes | `BillingPlan.PRO \| BillingPlan.FOUNDERS` | `@IsEnum([BillingPlan.PRO, BillingPlan.FOUNDERS])` |

## class AdminLoginDTO

- Source: `src/user/dto/adminLogin.dto.ts:4`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `email` | Yes | `string` | `@IsEmail` |
| `password` | Yes | `string` |  |
| `code` | Yes | `string` | `@MinLength(6)`<br>`@MaxLength(6)` |

## class AdminLoginResponse

- Source: `src/user/dto/adminLoginResponse.dto.ts:3`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `message` | Yes | `string` |  |
| `token` | No | `string` |  |

## class AdminNotification

- Source: `src/notifications/entities/adminNotification.entity.ts:12`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `adminNotificationId` | Yes | `string` | `@PrimaryGeneratedColumn('uuid', { name: 'admin_notification_id' })` |
| `type` | Yes | `string` | `@Column({ length: 50 })` |
| `message` | Yes | `string` | `@Column('text')` |
| `status` | No | `NotificationStatusType` | `@Column({ type: 'enum', enum: NotificationStatusType, default: NotificationStatusType.NEW, })` |
| `createdAt` | Yes | `Date` | `@CreateDateColumn({ name: 'created_at' })` |
| `updatedAt` | Yes | `Date` | `@UpdateDateColumn({ name: 'updated_at' })` |
| `deletedAt` | Yes | `Date` | `@DeleteDateColumn({ name: 'deleted_at' })` |

## class AdminUpdateUserRoleDTO

- Source: `src/user/dto/adminUpdateUserRole.dto.ts:4`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `userId` | Yes | `string` | `@IsUUID` |
| `roleId` | Yes | `number` | `@IsNumber` |

## class AdminUpdateUserStatusDTO

- Source: `src/user/dto/adminUpdateUserStatus.dto.ts:4`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `userId` | Yes | `string` | `@IsUUID` |
| `statusId` | Yes | `number` | `@IsNumber` |

## class AdminUser

- Source: `src/user/dto/admin-user.dto.ts:10`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `role` | Yes | `Role` |  |
| `userStatusId` | Yes | `number` |  |
| `userStatus` | Yes | `UserStatus` |  |
| `creatorStatusId` | Yes | `number` |  |
| `isAdmin` | Yes | `boolean` |  |
| `auth0Sub` | Yes | `string` |  |
| `isSocialLogin` | Yes | `boolean` |  |
| `paypalTrackingId` | Yes | `string` |  |
| `paypalMerchantId` | Yes | `string` |  |
| `userWallets` | Yes | `AdminWallet[]` |  |
| `negativePoints` | Yes | `number` |  |
| `socialMedia` | Yes | `SocialMedia[]` |  |

## class AdminWallet

- Source: `src/user/dto/public-wallet.dto.ts:22`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `userWalletId` | Yes | `string` |  |
| `signature` | Yes | `string` |  |

## class AffectedFolderDTO

- Source: `src/listing/dto/visibility-change-preview.dto.ts:4`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `id` | Yes | `string` |  |
| `name` | Yes | `string` |  |
| `type` | Yes | `FolderType` |  |

## class AgentAccessResponse

- Source: `src/agent/dto/marketplace-purchase.dto.ts:157`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `has_access` | Yes | `boolean` |  |
| `status` | Yes | `string` |  |
| `reason` | Yes | `string` |  |
| `download_url` | No | `string` |  |
| `expires_at` | No | `string` |  |
| `price` | No | `number` |  |
| `currency` | No | `string` |  |
| `purchase_url` | No | `string` |  |

## class AgentAddListingDto

- Source: `src/agent/dto/agent-folder.dto.ts:98`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `listing_id` | Yes | `string` | `@IsUUID` |

## class AgentAssetInfo

- Source: `src/agent/dto/agent-listing-response.dto.ts:84`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `asset_id` | Yes | `string` |  |
| `asset_type` | Yes | `string` |  |
| `file_name` | Yes | `string` |  |
| `url` | Yes | `string \| null` |  |
| `uploaded` | Yes | `boolean` |  |
| `failed` | Yes | `boolean` |  |
| `errors` | Yes | `{ fileName?: string; error: string }[]` |  |

## class AgentAssetsReadyResponse

- Source: `src/agent/dto/marketplace-purchase.dto.ts:211`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `listing_id` | Yes | `string` |  |
| `all_ready` | Yes | `boolean` |  |
| `issues` | Yes | `{ asset_id: string; errors: any[] \| null; failed: boolean; status: string; }[]` |  |

## class AgentAuditLog

- Source: `src/agent/entities/agent-audit-log.entity.ts:13`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `id` | Yes | `string` | `@PrimaryColumn({ type: 'uuid', name: 'id', default: () => 'gen_random_uuid()' })` |
| `agentId` | Yes | `string` | `@Column({ name: 'agent_id', type: 'uuid' })` |
| `action` | Yes | `string` | `@Column({ type: 'varchar', length: 50 })` |
| `details` | Yes | `Record<string, any>` | `@Column({ type: 'jsonb', default: '{}' })` |
| `ipAddress` | Yes | `string \| null` | `@Column({ name: 'ip_address', type: 'inet', nullable: true })` |
| `userAgent` | Yes | `string \| null` | `@Column({ name: 'user_agent', type: 'text', nullable: true })` |
| `createdAt` | Yes | `Date` | `@CreateDateColumn({ name: 'created_at', type: 'timestamptz' })` |
| `agent` | Yes | `User` | `@ManyToOne(() => User)`<br>`@JoinColumn({ name: 'agent_id' })` |

## class AgentBulkAddListingsDto

- Source: `src/agent/dto/agent-folder.dto.ts:103`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `listing_ids` | Yes | `string[]` | `@IsArray`<br>`@ArrayMinSize(1)`<br>`@ArrayMaxSize(100)`<br>`@IsUUID('all', { each: true })` |

## class AgentBulkRemoveListingsDto

- Source: `src/agent/dto/agent-folder.dto.ts:111`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `listing_ids` | Yes | `string[]` | `@IsArray`<br>`@ArrayMinSize(1)`<br>`@ArrayMaxSize(100)`<br>`@IsUUID('all', { each: true })` |

## class AgentCategoryResponse

- Source: `src/agent/dto/agent-listing-response.dto.ts:125`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `id` | Yes | `number` |  |
| `name` | Yes | `string` |  |
| `subcategories` | Yes | `{ id: number; name: string; tags: { id: number; name: string }[]; }[]` |  |

## interface AgentCommentResponse

- Source: `src/agent/dto/social-engagement.dto.ts:107`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `comment_id` | Yes | `string` |  |
| `comment` | Yes | `string` |  |
| `listing_id` | Yes | `string` |  |
| `user_id` | Yes | `string` |  |
| `user` | Yes | `AgentCommentUserResponse \| null` |  |
| `parent_id` | Yes | `string \| null` |  |
| `reply_to_comment_id` | Yes | `string \| null` |  |
| `replies` | Yes | `number` |  |
| `upvotes` | Yes | `number` |  |
| `downvotes` | Yes | `number` |  |
| `upvoted` | Yes | `boolean` |  |
| `downvoted` | Yes | `boolean` |  |
| `is_flagged` | Yes | `boolean` |  |
| `is_hidden` | Yes | `boolean` |  |
| `is_agent` | Yes | `boolean` |  |
| `edited` | Yes | `boolean` |  |
| `created_at` | Yes | `Date` |  |

## interface AgentCommentUserResponse

- Source: `src/agent/dto/social-engagement.dto.ts:100`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `user_id` | Yes | `string` |  |
| `user_name` | Yes | `string \| null` |  |
| `avatar` | Yes | `string \| null` |  |
| `is_agent` | Yes | `boolean` |  |

## interface AgentCommentVoteResponse

- Source: `src/agent/dto/social-engagement.dto.ts:138`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `comment_vote_id` | Yes | `string` |  |
| `user_id` | Yes | `string` |  |
| `comment_id` | Yes | `string` |  |
| `vote` | Yes | `VoteType` |  |
| `created_at` | Yes | `Date` |  |
| `updated_at` | Yes | `Date` |  |

## class AgentContractTypeResponse

- Source: `src/agent/dto/agent-listing-response.dto.ts:135`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `id` | Yes | `number` |  |
| `name` | Yes | `string` |  |

## class AgentCreateFolderDto

- Source: `src/agent/dto/agent-folder.dto.ts:17`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `name` | Yes | `string` | `@IsString`<br>`@MaxLength(100)` |
| `type` | Yes | `FolderType` | `@IsEnum(FolderType)` |
| `visibility` | No | `FolderVisibility` | `@IsEnum(FolderVisibility)`<br>`@IsOptional` |
| `thumbnail_url` | No | `string` | `@IsString`<br>`@MaxLength(2048)`<br>`@IsOptional` |
| `description` | No | `string` | `@IsString`<br>`@MaxLength(1000)`<br>`@IsOptional` |
| `tags` | No | `string[]` | `@IsArray`<br>`@ArrayMaxSize(20)`<br>`@IsString({ each: true })`<br>`@MaxLength(32, { each: true })`<br>`@IsOptional` |

## class AgentCreateListingResponse

- Source: `src/agent/dto/agent-listing-response.dto.ts:36`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `listing_id` | Yes | `string` |  |
| `upload_url` | No | `string` |  |
| `thumbnail_upload_url` | No | `string` |  |
| `warnings` | No | `string[]` |  |

## class AgentDownloadResponse

- Source: `src/agent/dto/marketplace-purchase.dto.ts:168`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `files` | Yes | `{ signed_url: string; file_name: string; content_length: number; }[]` |  |

## class AgentEnqueueFeedQueueDto

- Source: `src/agent/dto/feed-queue.dto.ts:4`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `target_type` | Yes | `FeedTargetType` | `@IsEnum(FeedTargetType)` |
| `target_id` | Yes | `string` | `@IsUUID` |

## class AgentEstimateBoth

- Source: `src/agent/dto/marketplace-purchase.dto.ts:137`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `listing_id` | Yes | `string` |  |
| `price` | Yes | `number` |  |
| `currency` | Yes | `string` |  |
| `estimates` | Yes | `{ download: { estimated_seller_net: number; currency: string; warning?: string; }; ownership: { estimated_seller_net: number; currency: string; warning?: string; }; }` |  |

## type AgentEstimateResponse

- Source: `src/agent/dto/marketplace-purchase.dto.ts:155`
- Type: `AgentEstimateSingle \| AgentEstimateBoth`

## class AgentEstimateSingle

- Source: `src/agent/dto/marketplace-purchase.dto.ts:128`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `listing_id` | Yes | `string` |  |
| `price` | Yes | `number` |  |
| `estimated_seller_net` | Yes | `number` |  |
| `currency` | Yes | `string` |  |
| `purchase_type` | Yes | `string` |  |
| `warning` | No | `string` |  |

## interface AgentFolderResponse

- Source: `src/folder/helpers/agent-folder-response.ts:4`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `id` | Yes | `string` |  |
| `name` | Yes | `string` |  |
| `description` | Yes | `string \| null` |  |
| `tags` | Yes | `string[] \| null` |  |
| `type` | Yes | `string` |  |
| `visibility` | Yes | `string` |  |
| `thumbnailUrl` | Yes | `string \| null` |  |
| `ownerId` | Yes | `string` |  |
| `url` | Yes | `string \| null` |  |
| `likeCount` | Yes | `number` |  |
| `saveCount` | Yes | `number` |  |
| `followCount` | Yes | `number` |  |
| `viralScore` | Yes | `number` |  |
| `listingCount` | Yes | `number` |  |
| `createdAt` | Yes | `Date` |  |
| `updatedAt` | Yes | `Date` |  |

## class AgentKeyRotationResponse

- Source: `src/agent/dto/agent-response.dto.ts:43`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `api_key` | Yes | `string` |  |

## class AgentListingCursorResponse

- Source: `src/agent/dto/agent-listing-response.dto.ts:78`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `listings` | Yes | `AgentListingSummary[]` |  |
| `page_info` | Yes | `AgentListingPageInfo` |  |
| `total_count` | Yes | `number` |  |

## class AgentListingDetailResponse

- Source: `src/agent/dto/agent-listing-response.dto.ts:94`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `listing_id` | Yes | `string` |  |
| `name` | Yes | `string` |  |
| `slug` | Yes | `string` |  |
| `description` | Yes | `string` |  |
| `status` | Yes | `string` |  |
| `price` | Yes | `string \| null` |  |
| `payment_method` | Yes | `string \| null` |  |
| `private` | Yes | `boolean` |  |
| `free_download` | Yes | `boolean` |  |
| `category` | Yes | `{ id: number; name: string }` |  |
| `contract_type` | Yes | `{ id: number; name: string }` |  |
| `tags` | Yes | `string[]` |  |
| `assets` | Yes | `AgentAssetInfo[]` |  |
| `listing_contract_id` | Yes | `number \| null` |  |
| `created_at` | Yes | `Date` |  |
| `listed_at` | Yes | `Date \| null` |  |
| `failure_reason` | No | `string` |  |
| `zip_manifest_summary` | No | `{ version: number; generated_at: string; total_files: number; total_size_bytes: number; types: Record< string, { count: number; size_bytes: number; extensions: string[] } >; manifest_url: string; }` |  |

## class AgentListingListResponse

- Source: `src/agent/dto/agent-listing-response.dto.ts:61`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `listings` | Yes | `AgentListingSummary[]` |  |
| `total` | Yes | `number` |  |
| `page` | Yes | `number` |  |
| `limit` | Yes | `number` |  |

## type AgentListingPageInfo
_`page_info` enforces the cursor invariant via a discriminated union: when `has_next_page` is true, `end_cursor` is guaranteed non-null (the agent has somewhere to advance to). When false, `end_cursor` is null (terminal page — no next cursor to track)._

- Source: `src/agent/dto/agent-listing-response.dto.ts:74`
- Type: `\| { has_next_page: true; end_cursor: string } \| { has_next_page: false; end_cursor: null }`

## class AgentListingQueryDto

- Source: `src/agent/dto/create-listing.dto.ts:127`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `status` | No | `string` | `@IsOptional`<br>`@IsString`<br>`@IsIn([ 'uploading', 'processing', 'pending_approval', 'failed', 'minting', 'minted', 'listed', 'rejected', 'deleted', 'discarded', 'cancelled', ])` |
| `page` | No | `number` | `@IsOptional`<br>`@Type(() => Number)`<br>`@IsNumber`<br>`@Min(1)` |
| `limit` | No | `number` | `@IsOptional`<br>`@Type(() => Number)`<br>`@IsNumber`<br>`@Min(1)`<br>`@Max(50)` |
| `first` | No | `number` | `@IsOptional`<br>`@Type(() => Number)`<br>`@IsInt`<br>`@Min(1)`<br>`@Max(50)` |
| `after` | No | `string` | `@IsOptional`<br>`@IsString` |

## class AgentListingStatusReferenceResponse

- Source: `src/agent/dto/agent-listing-response.dto.ts:140`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `id` | Yes | `number` |  |
| `name` | Yes | `string` |  |

## class AgentListingStatusResponse

- Source: `src/agent/dto/marketplace-purchase.dto.ts:205`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `listing_id` | Yes | `string` |  |
| `status` | Yes | `string` |  |
| `processing` | Yes | `string \| null` |  |

## class AgentListingSummary

- Source: `src/agent/dto/agent-listing-response.dto.ts:48`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `listing_id` | Yes | `string` |  |
| `name` | Yes | `string` |  |
| `slug` | Yes | `string` |  |
| `status` | Yes | `string` |  |
| `price` | Yes | `string \| null` |  |
| `private` | Yes | `boolean` |  |
| `free_download` | Yes | `boolean` |  |
| `category` | Yes | `string` |  |
| `created_at` | Yes | `Date` |  |
| `thumbnail_url` | Yes | `string \| null` |  |

## class AgentMetadataResponse

- Source: `src/agent/dto/marketplace-purchase.dto.ts:176`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `content_length` | Yes | `number` |  |
| `content_type` | Yes | `string` |  |
| `name` | Yes | `string` |  |

## class AgentMoveListingDto

- Source: `src/agent/dto/agent-folder.dto.ts:93`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `target_folder_id` | Yes | `string` | `@IsUUID` |

## class AgentOperator

- Source: `src/agent/entities/agent-operator.entity.ts:12`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `id` | Yes | `string` | `@PrimaryGeneratedColumn('uuid', { name: 'id' })` |
| `agentId` | Yes | `string` | `@Column({ name: 'agent_id', type: 'uuid' })` |
| `operatorId` | Yes | `string \| null` | `@Column({ name: 'operator_id', type: 'uuid', nullable: true })` |
| `operatorEmail` | Yes | `string \| null` | `@Column({ name: 'operator_email', type: 'varchar', length: 255, nullable: true })` |
| `status` | Yes | `string` | `@Column({ type: 'varchar', length: 20, default: 'active' })` |
| `linkedAt` | Yes | `Date \| null` | `@Column({ name: 'linked_at', type: 'timestamptz', nullable: true })` |
| `revokedAt` | Yes | `Date \| null` | `@Column({ name: 'revoked_at', type: 'timestamptz', nullable: true })` |
| `createdAt` | Yes | `Date` | `@CreateDateColumn({ name: 'created_at', type: 'timestamptz' })` |
| `updatedAt` | Yes | `Date` | `@UpdateDateColumn({ name: 'updated_at', type: 'timestamptz' })` |
| `agent` | Yes | `User` | `@ManyToOne(() => User)`<br>`@JoinColumn({ name: 'agent_id' })` |
| `operator` | Yes | `User` | `@ManyToOne(() => User)`<br>`@JoinColumn({ name: 'operator_id' })` |

## interface AgentPaginatedCommentsResponse

- Source: `src/agent/dto/social-engagement.dto.ts:127`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `comments` | Yes | `AgentCommentResponse[]` |  |
| `page_info` | Yes | `{ has_next_page: boolean; end_cursor: string \| null; }` |  |
| `total_count` | Yes | `number` |  |

## class AgentPerformanceDTO

- Source: `src/analytics/dto/agent-performance.dto.ts:3`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `agentListings` | Yes | `number` |  |
| `humanListings` | Yes | `number` |  |
| `agentConversionRate` | Yes | `number` |  |
| `humanConversionRate` | Yes | `number` |  |
| `agentAvgRevenue` | Yes | `number` |  |
| `humanAvgRevenue` | Yes | `number` |  |
| `period` | Yes | `string` |  |

## class AgentPerformanceQueryDto

- Source: `src/agent/dto/analytics-query.dto.ts:81`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `period` | No | `string` | `@IsOptional`<br>`@IsIn(['7d', '30d', '90d'])` |

## class AgentProfileResponse

- Source: `src/agent/dto/agent-response.dto.ts:15`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `agent_id` | Yes | `string` |  |
| `name` | Yes | `string` |  |
| `username` | Yes | `string` |  |
| `email` | Yes | `string` |  |
| `description` | Yes | `string \| null` |  |
| `avatar_url` | Yes | `string \| null` |  |
| `banner_url` | Yes | `string \| null` |  |
| `callback_url` | Yes | `string \| null` |  |
| `reputation_score` | Yes | `number` |  |
| `status` | Yes | `string` |  |
| `is_email_verified` | Yes | `boolean` |  |
| `rate_limits` | Yes | `{ requests_per_minute: number; }` |  |
| `paypal` | Yes | `{ merchant_connected: boolean; vault_connected: boolean; }` |  |
| `capabilities` | Yes | `{ can_browse: boolean; can_use_api: boolean; can_buy: boolean; can_sell: boolean; }` |  |
| `created_at` | Yes | `Date` |  |

## class AgentPublishResponse

- Source: `src/agent/dto/marketplace-purchase.dto.ts:199`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `message` | Yes | `string` |  |
| `listing_id` | No | `string` |  |
| `status` | No | `string` |  |

## class AgentPurchaseEntry

- Source: `src/agent/dto/marketplace-purchase.dto.ts:182`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `transaction_id` | Yes | `string` |  |
| `listing_id` | Yes | `string` |  |
| `amount` | Yes | `string` |  |
| `currency` | Yes | `string` |  |
| `purchase_type` | Yes | `string` |  |
| `status` | Yes | `string` |  |
| `created_at` | Yes | `Date` |  |

## class AgentPurchaseResponse

- Source: `src/agent/dto/marketplace-purchase.dto.ts:113`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `success` | Yes | `boolean` |  |
| `transaction_id` | No | `string` |  |
| `download_url` | No | `string` |  |
| `status` | No | `string` |  |
| `message` | No | `string` |  |

## class AgentPurchasesListResponse

- Source: `src/agent/dto/marketplace-purchase.dto.ts:192`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `purchases` | Yes | `AgentPurchaseEntry[]` |  |
| `total` | Yes | `number` |  |
| `page` | Yes | `number` |  |
| `limit` | Yes | `number` |  |

## class AgentPurchaseStatusResponse

- Source: `src/agent/dto/marketplace-purchase.dto.ts:121`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `status` | Yes | `string` |  |
| `transaction_id` | No | `string` |  |
| `download_url` | No | `string` |  |
| `message` | No | `string` |  |

## class AgentRegistrationResponse

- Source: `src/agent/dto/agent-response.dto.ts:1`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `agent_id` | Yes | `string` |  |
| `api_key` | Yes | `string` |  |
| `name` | Yes | `string` |  |
| `username` | Yes | `string` |  |
| `avatar_url` | Yes | `string` |  |
| `created_at` | Yes | `Date` |  |
| `email_verification_deadline` | Yes | `Date` |  |
| `rate_limits` | Yes | `{ requests_per_minute: number; }` |  |
| `status` | Yes | `string` |  |

## class AgentReorderFolderDto

- Source: `src/agent/dto/agent-folder.dto.ts:80`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `listing_id` | Yes | `string` | `@IsUUID` |
| `after_id` | No | `string` | `@IsUUID`<br>`@IsOptional` |
| `before_id` | No | `string` | `@IsUUID`<br>`@IsOptional` |

## class AgentReprocessResponse

- Source: `src/agent/dto/marketplace-purchase.dto.ts:222`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `listing_id` | Yes | `string` |  |
| `status` | Yes | `string` |  |
| `message` | Yes | `string` |  |

## class AgentSuccessRateDTO

- Source: `src/analytics/dto/agent-performance.dto.ts:27`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `userId` | Yes | `string` |  |
| `published` | Yes | `number` |  |
| `sold` | Yes | `number` |  |
| `conversionRate` | Yes | `number` |  |

## class AgentUpdateFolderDto

- Source: `src/agent/dto/agent-folder.dto.ts:47`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `name` | No | `string` | `@IsString`<br>`@MaxLength(100)`<br>`@IsOptional` |
| `visibility` | No | `FolderVisibility` | `@IsEnum(FolderVisibility)`<br>`@IsOptional` |
| `thumbnail_url` | No | `string` | `@IsString`<br>`@MaxLength(2048)`<br>`@IsOptional` |
| `type` | No | `FolderType` | `@IsEnum(FolderType)`<br>`@IsIn([FolderType.COLLECTION, FolderType.PLAYLIST])`<br>`@IsOptional` |
| `description` | No | `string` | `@IsString`<br>`@MaxLength(1000)`<br>`@IsOptional` |
| `tags` | No | `string[]` | `@IsArray`<br>`@ArrayMaxSize(20)`<br>`@IsString({ each: true })`<br>`@MaxLength(32, { each: true })`<br>`@IsOptional` |

## class AgentUploadConfirmResponse

- Source: `src/agent/dto/agent-listing-response.dto.ts:43`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `listing_id` | Yes | `string` |  |
| `status` | Yes | `string` |  |

## class AiModel

- Source: `src/ai-model/entities/aiModel.entity.ts:13`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `aiModelId` | Yes | `number` | `@PrimaryGeneratedColumn({ type: 'integer', name: 'ai_model_id' })` |
| `name` | Yes | `string` | `@Column('character varying', { name: 'name' })` |
| `isDisabled` | Yes | `boolean` | `@Column({ name: 'is_disabled', default: false })` |
| `sortOrder` | Yes | `number` | `@Column('integer', { name: 'sort_order', default: 0 })` |
| `aiModelToCategories` | Yes | `AiModelToCategory[]` | `@OneToMany(() => AiModelToCategory, (junction) => junction.aiModel, { eager: false, })` |
| `createdAt` | Yes | `Date` | `@CreateDateColumn({ name: 'created_at' })` |
| `updatedAt` | Yes | `Date` | `@UpdateDateColumn({ name: 'updated_at' })` |
| `deletedAt` | Yes | `Date` | `@DeleteDateColumn({ name: 'deleted_at' })` |

## class AiModelCategoryDTO

- Source: `src/ai-model/dto/aiModelResponse.dto.ts:3`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `categoryId` | Yes | `number` |  |
| `type` | Yes | `string` |  |

## class AiModelResponseDTO

- Source: `src/ai-model/dto/aiModelResponse.dto.ts:12`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `aiModelId` | Yes | `number` |  |
| `name` | Yes | `string` |  |
| `isDisabled` | Yes | `boolean` |  |
| `sortOrder` | Yes | `number` |  |
| `categories` | Yes | `AiModelCategoryDTO[]` |  |

## class AiModelToCategory

- Source: `src/ai-model/entities/aiModelToCategory.entity.ts:13`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `id` | Yes | `number` | `@PrimaryGeneratedColumn({ type: 'integer', name: 'id' })` |
| `aiModelId` | Yes | `number` | `@Column('integer', { name: 'ai_model_id' })` |
| `aiModel` | Yes | `AiModel` | `@ManyToOne(() => AiModel, (model) => model.aiModelToCategories)`<br>`@JoinColumn({ name: 'ai_model_id', referencedColumnName: 'aiModelId' })` |
| `categoryId` | Yes | `number` | `@Column('integer', { name: 'category_id' })` |
| `category` | Yes | `Category` | `@ManyToOne(() => Category)`<br>`@JoinColumn({ name: 'category_id', referencedColumnName: 'categoryId' })` |

## class AllPointEarnedWithTotalDTO

- Source: `src/point/dto/allPointEarnedWithTotal.dto.ts:4`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `pointEarned` | Yes | `PointEarned[]` |  |
| `total` | Yes | `number` |  |

## interface AnonymousEmail

- Source: `src/notifications/types/anonymous-email.interface.ts:1`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `subject` | Yes | `string` |  |
| `content` | Yes | `string` |  |
| `link` | Yes | `string` |  |
| `button` | Yes | `string` |  |
| `code` | No | `string` |  |

## class Appeal

- Source: `src/agent/entities/appeal.entity.ts:11`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `appealId` | Yes | `string` | `@PrimaryGeneratedColumn('uuid', { name: 'appeal_id' })` |
| `userId` | Yes | `string` | `@Column({ name: 'user_id', type: 'uuid' })` |
| `reason` | Yes | `string` | `@Column({ type: 'text' })` |
| `status` | Yes | `string` | `@Column({ type: 'varchar', length: 20, default: 'submitted' })` |
| `submittedAt` | Yes | `Date` | `@CreateDateColumn({ name: 'submitted_at', type: 'timestamptz' })` |
| `reviewedAt` | Yes | `Date \| null` | `@Column({ name: 'reviewed_at', type: 'timestamptz', nullable: true })` |
| `reviewedBy` | Yes | `string \| null` | `@Column({ name: 'reviewed_by', type: 'uuid', nullable: true })` |
| `reviewerNotes` | Yes | `string \| null` | `@Column({ name: 'reviewer_notes', type: 'text', nullable: true })` |
| `user` | Yes | `User` | `@ManyToOne(() => User)`<br>`@JoinColumn({ name: 'user_id' })` |

## class AppealResponse

- Source: `src/agent/dto/appeal.dto.ts:10`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `appeal_id` | Yes | `string` |  |
| `status` | Yes | `string` |  |
| `reason` | Yes | `string` |  |
| `submitted_at` | Yes | `Date` |  |
| `reviewed_at` | Yes | `Date \| null` |  |
| `reviewer_notes` | Yes | `string \| null` |  |

## class Asset

- Source: `src/listing/entities/asset.entity.ts:22`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `assetId` | Yes | `string` | `@PrimaryColumn('uuid', { name: 'asset_id' })` |
| `url` | Yes | `string` | `@Column('character varying', { name: 'url' })` |
| `assetTypeId` | Yes | `number` | `@Column({ name: 'asset_type_id' })` |
| `assetType` | Yes | `AssetType` | `@ManyToOne(() => AssetType, (assetType) => assetType.assets)`<br>`@JoinColumn({ name: 'asset_type_id', referencedColumnName: 'assetTypeId', })` |
| `userId` | Yes | `string` | `@Column({ name: 'user_id' })` |
| `user` | Yes | `User` | `@ManyToOne(() => User, (user) => user.assets)`<br>`@JoinColumn({ name: 'user_id', referencedColumnName: 'userId' })` |
| `listingToAssets` | Yes | `ListingToAsset[]` | `@OneToMany(() => ListingToAsset, (listingAssets) => listingAssets.asset)` |
| `failed` | No | `boolean` | `@Column({ nullable: true })` |
| `status` | No | `AssetStatusType` | `@Column({ type: 'enum', enum: AssetStatusType, nullable: true })` |
| `errors` | No | `string` | `@Column({ nullable: true })` |
| `uploaded` | No | `boolean` | `@Column({ nullable: true })` |
| `parentId` | Yes | `string \| null` | `@Column('uuid', { name: 'parent_id', nullable: true })` |
| `parent` | Yes | `Asset` | `@ManyToOne(() => Asset, (parent) => parent.relatedAssets, { onDelete: 'CASCADE', })`<br>`@JoinColumn({ name: 'parent_id', referencedColumnName: 'assetId' })` |
| `relatedAssets` | Yes | `Asset[]` | `@OneToMany(() => Asset, (reply) => reply.parent, { cascade: true })` |
| `videoFrames` | Yes | `AssetVideoFrame[]` | `@OneToMany(() => AssetVideoFrame, (frame) => frame.asset, { cascade: true })` |
| `lshBuckets` | Yes | `AssetLshBucket[]` | `@OneToMany(() => AssetLshBucket, (bucket) => bucket.asset, { cascade: true })` |
| `imageFingerprint` | No | `string` | `@Column({ name: 'image_fingerprint', type: 'text', nullable: true })` |
| `videoFingerprint` | No | `string` | `@Column({ name: 'video_fingerprint', type: 'text', nullable: true })` |
| `audioFingerprint` | No | `string` | `@Column({ name: 'audio_fingerprint', type: 'varchar', length: 64, nullable: true, })` |
| `zipFingerprint` | No | `string` | `@Column({ name: 'zip_fingerprint', type: 'text', nullable: true, })` |
| `videoSignature` | No | `string` | `@Column({ name: 'video_signature', type: 'varchar', length: 100, nullable: true, })` |
| `audioSignature` | No | `string` | `@Column({ name: 'audio_signature', type: 'varchar', length: 64, nullable: true, })` |
| `formats` | Yes | `string[]` | `@Column('simple-array', { name: 'formats', nullable: true })` |
| `width` | No | `number` | `@Column({ nullable: true })` |
| `height` | No | `number` | `@Column({ nullable: true })` |
| `duration` | No | `number` | `@Column({ type: 'float', nullable: true })` |
| `fps` | No | `number` | `@Column({ type: 'float', nullable: true })` |
| `codec` | No | `string` | `@Column('character varying', { nullable: true })` |
| `bitrate` | No | `number` | `@Column({ type: 'int', nullable: true })` |
| `sampleRate` | No | `number` | `@Column({ name: 'sample_rate', type: 'int', nullable: true })` |
| `contentLength` | No | `number` | `@Column('bigint', { name: 'content_length', nullable: true })` |
| `contentType` | No | `string` | `@Column('character varying', { name: 'content_type', nullable: true })` |
| `name` | No | `string \| null` |  |
| `description` | No | `string \| null` |  |
| `thumbnailUrl` | No | `string \| null` |  |
| `assetTypeName` | No | `string \| null` |  |
| `parentListingId` | No | `string \| null` |  |
| `parentListingName` | No | `string \| null` |  |
| `createdAt` | Yes | `Date` | `@CreateDateColumn({ name: 'created_at' })` |
| `updatedAt` | Yes | `Date` | `@UpdateDateColumn({ name: 'updated_at' })` |
| `deletedAt` | Yes | `Date` | `@DeleteDateColumn({ name: 'deleted_at' })` |

## class AssetAccessResponse

- Source: `src/listing/dto/asset-access-response.dto.ts:22`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `hasAccess` | Yes | `boolean` |  |
| `status` | Yes | `AccessStatus` |  |
| `reason` | Yes | `string` |  |
| `downloadUrl` | No | `string` |  |
| `expiresAt` | No | `Date` |  |
| `price` | No | `number` |  |
| `currency` | No | `string` |  |
| `purchaseUrl` | No | `string` |  |

## class AssetDTO

- Source: `src/listing/dto/asset.dto.ts:5`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `assetId` | Yes | `string` |  |
| `url` | Yes | `string` |  |
| `type` | Yes | `string` |  |
| `status` | Yes | `string` |  |
| `assetTypeId` | Yes | `number` |  |
| `parentId` | No | `string` |  |
| `failed` | No | `boolean` |  |
| `errors` | Yes | `AssetError[]` |  |
| `uploaded` | No | `boolean` |  |
| `nsfw` | No | `boolean` |  |
| `likely` | No | `boolean` |  |
| `duplicate` | No | `boolean` |  |
| `relatedAssets` | No | `RelatedAssets[]` |  |
| `formats` | No | `string[]` |  |
| `width` | No | `number` |  |
| `height` | No | `number` |  |
| `duration` | No | `number` |  |
| `bitrate` | No | `number` |  |
| `codec` | No | `string` |  |
| `contentLength` | No | `number` |  |
| `contentType` | No | `string` |  |

## class AssetError

- Source: `src/listing/dto/asset.dto.ts:112`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `fileName` | Yes | `string` |  |
| `error` | Yes | `string` |  |

## class AssetFlag

- Source: `src/listing/entities/assetFlag.entity.ts:16`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `assetFlagId` | Yes | `string` | `@PrimaryGeneratedColumn('uuid', { name: 'asset_flag_id' })` |
| `assetId` | Yes | `string \| null` | `@Column('uuid', { name: 'asset_id', nullable: true })` |
| `url` | Yes | `string` | `@Column('character varying', { name: 'url', nullable: true })` |
| `assetTypeId` | Yes | `number` | `@Column({ name: 'asset_type_id', nullable: true })` |
| `assetType` | Yes | `AssetType` | `@ManyToOne(() => AssetType, (assetType) => assetType.assetFlags)`<br>`@JoinColumn({ name: 'asset_type_id', referencedColumnName: 'assetTypeId', })` |
| `likely` | No | `boolean` | `@Column({ nullable: true, default: null })` |
| `violation` | Yes | `string` | `@Column({ length: 250 })` |
| `decision` | Yes | `string` | `@Column({ nullable: true })` |
| `negativePoints` | Yes | `number` | `@Column({ name: 'negative_points', nullable: true, })` |
| `status` | No | `FlagType` | `@Column({ type: 'enum', enum: FlagType })` |
| `userId` | Yes | `string` | `@Column({ name: 'user_id' })` |
| `user` | Yes | `User` | `@ManyToOne(() => User, (user) => user.assetFlags)`<br>`@JoinColumn({ name: 'user_id', referencedColumnName: 'userId' })` |
| `createdAt` | Yes | `Date` | `@CreateDateColumn({ name: 'created_at' })` |
| `updatedAt` | Yes | `Date` | `@UpdateDateColumn({ name: 'updated_at' })` |
| `deletedAt` | Yes | `Date` | `@DeleteDateColumn({ name: 'deleted_at' })` |

## class AssetFlagDTO

- Source: `src/listing/dto/assetFlag.dto.ts:6`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `assetFlagId` | Yes | `string` |  |
| `url` | Yes | `string` |  |
| `key` | Yes | `string` |  |
| `violation` | Yes | `string` |  |
| `decision` | Yes | `string` |  |
| `userId` | Yes | `string` |  |
| `user` | Yes | `AdminUser` |  |
| `negativePoints` | Yes | `number` |  |
| `likely` | No | `boolean` |  |
| `status` | No | `string` |  |
| `createdAt` | Yes | `Date` |  |

## class AssetFlagResponseWithTotalDTO

- Source: `src/listing/dto/assetFlagResponseWithTotal.dto.ts:4`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `flags` | Yes | `AssetFlagDTO[]` |  |
| `total` | Yes | `number` |  |

## class AssetLshBucket

- Source: `src/listing/entities/assetLshBucket.entity.ts:13`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `id` | Yes | `number` | `@PrimaryGeneratedColumn({ name: 'id' })` |
| `assetId` | Yes | `string` | `@Column('uuid', { name: 'asset_id' })` |
| `asset` | Yes | `Asset` | `@ManyToOne(() => Asset, (asset) => asset.lshBuckets, { onDelete: 'CASCADE', })`<br>`@JoinColumn({ name: 'asset_id', referencedColumnName: 'assetId' })` |
| `bucketKey` | Yes | `string` | `@Column({ name: 'bucket_key', type: 'varchar', length: 100 })` |
| `createdAt` | Yes | `Date` | `@CreateDateColumn({ name: 'created_at' })` |

## type AssetPresentationShape

- Source: `src/listing/utils/assetPresentation.utils.ts:11`
- Type: `Pick< Asset, 'assetId' \| 'assetTypeId' \| 'url' \| 'parentId' \| 'contentType' >`

## class AssetStatusResponse

- Source: `src/listing/dto/asset-access-response.dto.ts:13`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `hasAccess` | Yes | `boolean` |  |
| `status` | Yes | `AccessStatus` |  |

## enum AssetStatusType

- Source: `src/utils/types.ts:80`

| Member | Value |
|---|---|
| `PENDING` | `'pending'` |
| `CHECKED` | `'checked'` |

## class AssetType

- Source: `src/listing/entities/assetType.entity.ts:14`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `assetTypeId` | Yes | `number` | `@PrimaryGeneratedColumn({ name: 'asset_type_id' })` |
| `name` | Yes | `string` | `@Column('character varying', { name: 'name' })` |
| `assets` | Yes | `Asset[]` | `@OneToMany(() => Asset, (assets) => assets.assetType)` |
| `assetFlags` | Yes | `AssetFlag[]` | `@OneToMany(() => AssetFlag, (assetFlags) => assetFlags.assetType)` |
| `createdAt` | Yes | `Date` | `@CreateDateColumn({ name: 'created_at' })` |
| `updatedAt` | Yes | `Date` | `@UpdateDateColumn({ name: 'updated_at' })` |
| `deletedAt` | Yes | `Date` | `@DeleteDateColumn({ name: 'deleted_at' })` |

## class AssetVideoFrame

- Source: `src/listing/entities/assetVideoFrame.entity.ts:14`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `id` | Yes | `number` | `@PrimaryGeneratedColumn({ name: 'id' })` |
| `assetId` | Yes | `string` | `@Column('uuid', { name: 'asset_id' })` |
| `asset` | Yes | `Asset` | `@ManyToOne(() => Asset, (asset) => asset.videoFrames, { onDelete: 'CASCADE', })`<br>`@JoinColumn({ name: 'asset_id', referencedColumnName: 'assetId' })` |
| `frameIndex` | Yes | `number` | `@Column({ name: 'frame_index' })` |
| `frameHash` | Yes | `string` | `@Column({ name: 'frame_hash', type: 'text' })` |
| `createdAt` | Yes | `Date` | `@CreateDateColumn({ name: 'created_at' })` |

## class AuctionCanceledDTO

- Source: `src/auction/dto/auctionCanceled.dto.ts:4`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `transactionHash` | Yes | `string` | `@IsString` |
| `blockNumber` | Yes | `number` | `@IsNumber` |
| `tokenId` | Yes | `number` | `@IsNumber` |

## class AuctionCreatedDTO

- Source: `src/auction/dto/auctionCreated.dto.ts:4`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `transactionHash` | Yes | `string` | `@IsString` |
| `blockNumber` | Yes | `number` | `@IsNumber` |
| `tokenId` | Yes | `number` | `@IsNumber` |

## class AuctionResultedDTO

- Source: `src/auction/dto/auctionResulted.dto.ts:4`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `transactionHash` | Yes | `string` | `@IsString` |
| `blockNumber` | Yes | `number` | `@IsNumber` |
| `tokenId` | Yes | `number` | `@IsNumber` |
| `oldOwnerC` | Yes | `string` | `@IsEthereumAddress` |
| `winnerC` | Yes | `string` | `@IsEthereumAddress` |
| `unitPrice` | Yes | `string` | `@IsString` |
| `winningBid` | Yes | `string` | `@IsString` |
| `payToken` | Yes | `string` | `@IsEthereumAddress` |

## class AuctionUpdateEndTimeDTO

- Source: `src/auction/dto/auctionUpdateEndTime.dto.ts:4`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `transactionHash` | Yes | `string` | `@IsString` |
| `blockNumber` | Yes | `number` | `@IsNumber` |
| `tokenId` | Yes | `number` | `@IsNumber` |
| `endTime` | Yes | `string` | `@IsString` |

## class AuctionUpdateRservePriceDTO

- Source: `src/auction/dto/auctionUpdateReservePrice.dto.ts:4`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `transactionHash` | Yes | `string` | `@IsString` |
| `blockNumber` | Yes | `number` | `@IsNumber` |
| `tokenId` | Yes | `number` | `@IsNumber` |
| `reservePrice` | Yes | `string` | `@IsString` |

## class AuctionUpdateStartTimeDTO

- Source: `src/auction/dto/auctionUpdateStartTime.dto.ts:4`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `transactionHash` | Yes | `string` | `@IsString` |
| `blockNumber` | Yes | `number` | `@IsNumber` |
| `tokenId` | Yes | `number` | `@IsNumber` |
| `startTime` | Yes | `string` |  |

## type Auth

- Source: `src/auth/better-auth.config.ts:558`
- Type: `typeof auth`

## class AuthorizePayPalPaymentDTO

- Source: `src/paypal/dto/authorizePayPalPayment.dto.ts:4`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `listingId` | Yes | `string` | `@IsString`<br>`@IsUUID` |
| `price` | Yes | `number` | `@IsNumber({ maxDecimalPlaces: 2 })`<br>`@Min(0)` |
| `deadline` | Yes | `number` | `@IsNumber` |

## interface BetterAuthAPIError

- Source: `src/user/user.service.ts:135`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `status` | Yes | `string \| number` |  |
| `statusCode` | Yes | `number` |  |
| `message` | Yes | `string` |  |
| `body` | No | `Record<string, any>` |  |

## class Bid

- Source: `src/auction/entities/bid.entity.ts:17`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `bidId` | Yes | `string` | `@PrimaryGeneratedColumn('uuid', { name: 'bid_id' })` |
| `listingId` | Yes | `string` | `@Column({ name: 'listing_id' })` |
| `listing` | Yes | `Listing` | `@ManyToOne(() => Listing, (listing) => listing.bids)`<br>`@JoinColumn({ name: 'listing_id', referencedColumnName: 'listingId' })` |
| `bidderId` | Yes | `string` | `@Column({ name: 'bidder_id' })` |
| `bidder` | Yes | `User` | `@ManyToOne(() => User, (bidder) => bidder.bids)`<br>`@JoinColumn({ name: 'bidder_id', referencedColumnName: 'userId' })` |
| `bid` | Yes | `number` | `@Column('integer')` |
| `blockNumber` | Yes | `number` | `@Column('bigint', { name: 'block_number' })` |
| `paymentToken` | Yes | `string` | `@Column('character varying', { name: 'payment_token', nullable: true })` |
| `auctionActive` | Yes | `boolean` | `@Column({ name: 'auction_active', default: true, })` |
| `withdrawn` | Yes | `boolean` | `@Column({ name: 'withdrawn', default: false, })` |
| `txHash` | Yes | `string` | `@Column('character varying', { name: 'tx_hash' })` |
| `createdAt` | Yes | `Date` | `@CreateDateColumn({ name: 'created_at' })` |
| `updatedAt` | Yes | `Date` | `@UpdateDateColumn({ name: 'updated_at' })` |
| `deletedAt` | Yes | `Date` | `@DeleteDateColumn({ name: 'deleted_at' })` |

## class BidDTO

- Source: `src/auction/dto/bid.dto.ts:6`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `bidId` | Yes | `string` |  |
| `listingId` | Yes | `string` |  |
| `listing` | Yes | `ListingDTO` |  |
| `bidderId` | Yes | `string` |  |
| `bidder` | Yes | `PublicUser` |  |
| `bid` | Yes | `number` |  |
| `blockNumber` | Yes | `number` |  |
| `paymentToken` | Yes | `string` |  |
| `auctionActive` | Yes | `boolean` |  |
| `withdrawn` | Yes | `boolean` |  |
| `txHash` | Yes | `string` |  |
| `createdAt` | Yes | `Date` |  |

## class BidPeriodQueryDto

- Source: `src/agent/dto/auction.dto.ts:22`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `period` | No | `string` | `@IsOptional`<br>`@IsString` |

## class BidPlacedDTO

- Source: `src/auction/dto/bidPlaced.dto.ts:4`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `transactionHash` | Yes | `string` | `@IsString` |
| `blockNumber` | Yes | `number` | `@IsNumber` |
| `tokenId` | Yes | `number` | `@IsNumber` |
| `bidderC` | Yes | `string` | `@IsEthereumAddress` |
| `bid` | Yes | `string` | `@IsString` |

## class BidsResponseDTO

- Source: `src/auction/dto/bidsResponse.dto.ts:5`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `bids` | Yes | `BidDTO[]` |  |
| `totalBids` | Yes | `ItemsByDateDTO[]` |  |
| `lifetimeBids` | Yes | `ItemsByDateDTO[]` |  |
| `totalGrowth` | Yes | `number` |  |
| `lifetimeGrowth` | Yes | `number` |  |

## class BidsTotalDTO

- Source: `src/auction/dto/bidsTotal.dto.ts:3`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `receivedBids` | Yes | `number` |  |
| `placedBids` | Yes | `number` |  |

## enum BillingInterval

- Source: `src/billing/billing.enums.ts:14`

| Member | Value |
|---|---|
| `MONTHLY` | `'monthly'` |
| `YEARLY` | `'yearly'` |

## enum BillingPlan

- Source: `src/billing/billing.enums.ts:1`

| Member | Value |
|---|---|
| `FREE` | `'free'` |
| `PRO` | `'pro'` |
| `FOUNDERS` | `'founders'` |

## enum BillingStatus

- Source: `src/billing/billing.enums.ts:7`

| Member | Value |
|---|---|
| `ACTIVE` | `'active'` |
| `PAST_DUE` | `'past_due'` |
| `CANCELED` | `'canceled'` |
| `INCOMPLETE` | `'incomplete'` |

## class BillingSubscription
_@deprecated Legacy dual-subscription field. New yearly users use mixed-interval subscriptions and this column stays null. Only populated for legacy yearly users created before the mixed-interval migration. Remove after all legacy subscriptions have expired (~12 months after migration)._

- Source: `src/billing/entities/billing-subscription.entity.ts:17`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `id` | Yes | `string` | `@PrimaryGeneratedColumn('uuid', { name: 'id' })` |
| `userId` | Yes | `string` | `@Column({ name: 'user_id', unique: true })` |
| `user` | Yes | `User` | `@OneToOne(() => User, (user) => user.billingSubscription)`<br>`@JoinColumn({ name: 'user_id', referencedColumnName: 'userId' })` |
| `stripeSubscriptionId` | No | `string` | `@Column({ name: 'stripe_subscription_id', nullable: true })` |
| `stripeCustomerId` | No | `string` | `@Column({ name: 'stripe_customer_id', nullable: true })` |
| `plan` | Yes | `BillingPlan` | `@Column({ name: 'plan', type: 'enum', enum: BillingPlan, default: BillingPlan.FREE, })` |
| `lastPaidTier` | Yes | `string \| null` | `@Column({ name: 'last_paid_tier', type: 'varchar', length: 20, nullable: true, })` |
| `status` | Yes | `BillingStatus` | `@Column({ name: 'status', type: 'enum', enum: BillingStatus, default: BillingStatus.ACTIVE, })` |
| `billingInterval` | Yes | `BillingInterval` | `@Column({ name: 'billing_interval', type: 'enum', enum: BillingInterval, default: BillingInterval.MONTHLY, })` |
| `creditSubscriptionId` | Yes | `string \| null` | `@Column({ name: 'credit_subscription_id', type: 'varchar', length: 255, nullable: true, })` |
| `currentPeriodEnd` | No | `Date` | `@Column({ name: 'current_period_end', type: 'timestamptz', nullable: true })` |
| `pendingDowngrade` | Yes | `string \| null` | `@Column({ name: 'pending_downgrade', type: 'varchar', length: 20, nullable: true, })` |
| `createdAt` | Yes | `Date` | `@CreateDateColumn({ name: 'created_at' })` |
| `updatedAt` | Yes | `Date` | `@UpdateDateColumn({ name: 'updated_at' })` |

## class BulkAddListingsInput

- Source: `src/folder/dto/bulk-add-listings.dto.ts:4`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `listingIds` | Yes | `string[]` | `@IsArray`<br>`@ArrayMinSize(1)`<br>`@ArrayMaxSize(100)`<br>`@IsUUID('all', { each: true })` |

## interface BulkAddResult

- Source: `src/folder/helpers/agent-folder-response.ts:23`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `added` | Yes | `number` |  |

## class BulkAddResultType
_GraphQL object types for bulk folder operations. Mirror the REST response shapes returned by FolderFacadeService.bulkAddListings / bulkRemoveListings (Task 4.5) so the schema and REST clients agree on the wire format._

- Source: `src/folder/dto/bulk-result.dto.ts:9`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `added` | Yes | `number` |  |

## interface BulkExportJobData

- Source: `src/analytics/analytics.processor.ts:24`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `userId` | Yes | `string` |  |
| `listingIds` | No | `string[]` |  |
| `dateFrom` | No | `string` |  |
| `dateTo` | No | `string` |  |
| `format` | Yes | `string` |  |

## class BulkExportRequestDto

- Source: `src/agent/dto/bulk-export-request.dto.ts:10`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `listing_ids` | No | `string[]` | `@IsOptional`<br>`@IsArray`<br>`@ArrayMaxSize(100)`<br>`@IsUUID('all', { each: true })` |
| `date_from` | No | `string` | `@IsOptional`<br>`@IsDateString` |
| `date_to` | No | `string` | `@IsOptional`<br>`@IsDateString` |
| `format` | No | `string` | `@IsOptional`<br>`@IsIn(['csv'])` |

## class BulkExportRequestInput

- Source: `src/analytics/dto/bulk-export.dto.ts:3`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `listingIds` | No | `string[]` |  |
| `dateFrom` | No | `string` |  |
| `dateTo` | No | `string` |  |
| `format` | Yes | `string` |  |

## class BulkExportStatusDTO

- Source: `src/analytics/dto/bulk-export.dto.ts:18`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `exportId` | Yes | `string` |  |
| `status` | Yes | `string` |  |
| `downloadUrl` | No | `string` |  |
| `error` | No | `string` |  |
| `requestedAt` | Yes | `Date` |  |

## class BulkRemoveListingsInput

- Source: `src/folder/dto/bulk-remove-listings.dto.ts:4`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `listingIds` | Yes | `string[]` | `@IsArray`<br>`@ArrayMinSize(1)`<br>`@ArrayMaxSize(100)`<br>`@IsUUID('all', { each: true })` |

## interface BulkRemoveResult

- Source: `src/folder/helpers/agent-folder-response.ts:27`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `removed` | Yes | `number` |  |

## class BulkRemoveResultType

- Source: `src/folder/dto/bulk-result.dto.ts:15`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `removed` | Yes | `number` |  |

## class BuyLinkDTO

- Source: `src/paypal/dto/buyLink.dto.ts:3`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `id` | Yes | `string` |  |
| `ids` | Yes | `string[]` |  |
| `expiresAt` | No | `string` |  |

## class BuyListingDto

- Source: `src/agent/dto/marketplace-purchase.dto.ts:16`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `transfer_ownership` | No | `boolean` | `@IsOptional`<br>`@IsBoolean` |
| `idempotency_key` | Yes | `string` | `@IsString`<br>`@IsNotEmpty`<br>`@IsUUID` |

## type CacheClient

- Source: `src/user/profile-counts.cache.ts:5`
- Type: `RedisClientType \| RedisClusterType`

## interface CallbackJobData

- Source: `src/agent/processors/agent-callback.processor.ts:14`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `agentId` | Yes | `string` |  |
| `callbackUrl` | Yes | `string` |  |
| `payload` | Yes | `Record<string, any>` |  |

## class CancelBidDto

- Source: `src/agent/dto/auction.dto.ts:14`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `listing_id` | Yes | `string` | `@IsUUID` |
| `bid` | Yes | `number` | `@IsNumber` |

## class Category

- Source: `src/listing/entities/category.entity.ts:16`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `categoryId` | Yes | `number` | `@PrimaryGeneratedColumn({ name: 'category_id' })` |
| `type` | Yes | `string` | `@Column('character varying', { name: 'type', nullable: true })` |
| `icon` | Yes | `string` | `@Column('character varying', { name: 'icon', nullable: true })` |
| `smallIcon` | Yes | `string` | `@Column('character varying', { name: 'small_icon', nullable: true })` |
| `loc` | Yes | `number` | `@Column({ name: 'loc', nullable: true })` |
| `parentId` | Yes | `number` | `@Column({ name: 'parent_id', nullable: true })` |
| `parent` | Yes | `Category` | `@ManyToOne(() => Category, (category) => category.subcategories)`<br>`@JoinColumn([{ name: 'parent_id', referencedColumnName: 'categoryId' }])` |
| `subcategories` | Yes | `Category[]` | `@OneToMany(() => Category, (category) => category.parent)` |
| `listings` | Yes | `Listing[]` | `@OneToMany(() => Listing, (listings) => listings.category)` |
| `listingToSubcategories` | Yes | `ListingToSubcategory[]` | `@OneToMany(() => ListingToSubcategory, (listingToSubcategory) => listingToSubcategory.subcategory)` |
| `createdAt` | Yes | `Date` | `@CreateDateColumn({ name: 'created_at' })` |
| `updatedAt` | Yes | `Date` | `@UpdateDateColumn({ name: 'updated_at' })` |
| `deletedAt` | Yes | `Date` | `@DeleteDateColumn({ name: 'deleted_at' })` |

## class CategoryStats

- Source: `src/analytics/entities/category-stats.entity.ts:3`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `categoryId` | Yes | `number` | `@PrimaryColumn({ name: 'category_id', type: 'int' })` |
| `period` | Yes | `string` | `@PrimaryColumn({ name: 'period', type: 'varchar', length: 10 })` |
| `salesCount` | Yes | `number` | `@Column({ name: 'sales_count', type: 'int', default: 0 })` |
| `totalRevenue` | Yes | `number` | `@Column({ name: 'total_revenue', type: 'numeric', precision: 12, scale: 2, default: 0 })` |
| `floorPrice` | Yes | `number` | `@Column({ name: 'floor_price', type: 'numeric', precision: 12, scale: 2, nullable: true })` |
| `medianPrice` | Yes | `number` | `@Column({ name: 'median_price', type: 'numeric', precision: 12, scale: 2, nullable: true })` |
| `ceilingPrice` | Yes | `number` | `@Column({ name: 'ceiling_price', type: 'numeric', precision: 12, scale: 2, nullable: true })` |
| `growthPct` | Yes | `number` | `@Column({ name: 'growth_pct', type: 'numeric', precision: 5, scale: 2, nullable: true })` |
| `newListingsCount` | Yes | `number` | `@Column({ name: 'new_listings_count', type: 'int', default: 0 })` |
| `computedAt` | Yes | `Date` | `@Column({ name: 'computed_at', type: 'timestamptz' })` |

## class CategoryStatsDTO

- Source: `src/analytics/dto/category-stats.dto.ts:3`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `categoryId` | Yes | `number` |  |
| `categoryName` | No | `string` |  |
| `salesCount` | Yes | `number` |  |
| `totalRevenue` | Yes | `number` |  |
| `floorPrice` | No | `number` |  |
| `medianPrice` | No | `number` |  |
| `ceilingPrice` | No | `number` |  |
| `growthPct` | No | `number` |  |
| `newListingsCount` | Yes | `number` |  |
| `period` | Yes | `string` |  |

## type CategoryType

- Source: `src/utils/types.ts:5`
- Type: `'Image' \| 'Video' \| 'Audio' \| 'Zip'`

## class ChainCall

- Source: `src/chain-call/entities/chainCall.entity.ts:11`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `chainCallId` | Yes | `string` | `@PrimaryGeneratedColumn('uuid', { name: 'chain_call_id' })` |
| `tokenId` | Yes | `number \| null` | `@Column({ name: 'token_id', nullable: true })` |
| `action` | Yes | `string` | `@Column({ name: 'action' })` |
| `eventDetails` | Yes | `EventData` | `@Column('json', { name: 'event_details' })` |
| `failed` | Yes | `string` | `@Column({ name: 'failed', nullable: true })` |
| `txHash` | Yes | `string` | `@Column({ name: 'tx_hash', nullable: true })` |
| `repeats` | Yes | `number` | `@Column({ name: 'repeats', default: 0 })` |
| `createdAt` | Yes | `Date` | `@CreateDateColumn({ name: 'created_at' })` |
| `updatedAt` | Yes | `Date` | `@UpdateDateColumn({ name: 'updated_at' })` |
| `deletedAt` | Yes | `Date` | `@DeleteDateColumn({ name: 'deleted_at' })` |

## enum ChainCallAction

- Source: `src/utils/types.ts:102`

| Member | Value |
|---|---|
| `CREATE_OFFER` | `'create-offer'` |
| `ACCEPT_OFFER` | `'accept-offer'` |
| `CANCEL_OFFER` | `'cancel-offer'` |
| `TRANSFER_OFFER` | `'transfer-offer'` |
| `MINT_LISTING` | `'mint-listing'` |

## class Check2faDTO

- Source: `src/user/dto/check2fa.dto.ts:4`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `code` | Yes | `string` | `@MinLength(6)`<br>`@MaxLength(6)` |

## class CheckoutUrlDTO

- Source: `src/billing/dto/billing.dto.ts:140`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `url` | Yes | `string` |  |

## interface CircuitBreakerConfig
_Percentage of failures in the rolling window to trip the circuit. Default: 50_

- Source: `src/resilience/circuit-breaker/circuit-breaker.types.ts:1`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `errorThresholdPercentage` | No | `number` |  |
| `resetTimeout` | No | `number` |  |
| `rollingCountTimeout` | No | `number` |  |
| `volumeThreshold` | No | `number` |  |
| `timeout` | No | `number` |  |
| `isFailure` | No | `(error: any) => boolean` |  |

## interface ClaimUrlResponse

- Source: `src/agent/dto/link-complete.dto.ts:9`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `claim_url` | Yes | `string` |  |
| `expires_in` | Yes | `number` |  |
| `expires_at` | Yes | `string` |  |

## type ClientData

- Source: `src/utils/clientData.ts:1`
- Type: `{ userId: string; fnName: string; data: any; }`

## class Comment

- Source: `src/activity/entities/comment.entity.ts:20`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `commentId` | Yes | `string` | `@PrimaryGeneratedColumn('uuid', { name: 'comment_id' })` |
| `comment` | Yes | `string` | `@Column('character varying', { length: 1000 })` |
| `listingId` | Yes | `string` | `@Column({ name: 'listing_id' })` |
| `listing` | Yes | `Listing` | `@ManyToOne(() => Listing, (listing) => listing.comments)`<br>`@JoinColumn({ name: 'listing_id', referencedColumnName: 'listingId' })` |
| `userId` | Yes | `string` | `@Column({ name: 'user_id' })` |
| `user` | Yes | `User` | `@ManyToOne(() => User, (user) => user.comments)`<br>`@JoinColumn({ name: 'user_id', referencedColumnName: 'userId' })` |
| `parentId` | Yes | `string` | `@Column({ name: 'parent_id', nullable: true })` |
| `parent` | Yes | `Comment` | `@ManyToOne(() => Comment, (parent) => parent.replies, { onDelete: 'CASCADE' })`<br>`@JoinColumn({ name: 'parent_id', referencedColumnName: 'commentId' })` |
| `replies` | Yes | `Comment[]` | `@OneToMany(() => Comment, (reply) => reply.parent, { cascade: true })` |
| `replyToCommentId` | Yes | `string` | `@Column({ name: 'reply_to_comment_id', nullable: true })` |
| `replyToComment` | Yes | `Comment` | `@ManyToOne(() => Comment, { onDelete: 'SET NULL' })`<br>`@JoinColumn({ name: 'reply_to_comment_id', referencedColumnName: 'commentId' })` |
| `votes` | Yes | `CommentVote[]` | `@OneToMany(() => CommentVote, (votes) => votes.comment, { cascade: true })` |
| `flags` | Yes | `CommentFlag[]` | `@OneToMany(() => CommentFlag, (flags) => flags.comment, { cascade: true })` |
| `createdAt` | Yes | `Date` | `@CreateDateColumn({ name: 'created_at' })` |
| `updatedAt` | Yes | `Date` | `@UpdateDateColumn({ name: 'updated_at' })` |
| `deletedAt` | Yes | `Date` | `@DeleteDateColumn({ name: 'deleted_at' })` |

## class CommentDTO

- Source: `src/activity/dto/comment.dto.ts:8`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `commentId` | Yes | `string` |  |
| `comment` | Yes | `string` |  |
| `listingId` | Yes | `string` |  |
| `listing` | No | `ListingDTO` |  |
| `userId` | Yes | `string` |  |
| `user` | Yes | `PublicUser` |  |
| `parentId` | Yes | `string` |  |
| `replyToCommentId` | No | `string` |  |
| `parent` | No | `CommentDTO` |  |
| `replies` | No | `number` |  |
| `upvotes` | Yes | `number` |  |
| `downvotes` | Yes | `number` |  |
| `upvoted` | Yes | `boolean` |  |
| `downvoted` | Yes | `boolean` |  |
| `isFlagged` | No | `boolean` |  |
| `isHidden` | No | `boolean` |  |
| `isAgent` | No | `boolean` |  |
| `edited` | Yes | `boolean` |  |
| `createdAt` | Yes | `Date` |  |

## class CommentFlag

- Source: `src/activity/entities/commentFlag.entity.ts:18`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `commentFlagId` | Yes | `string` | `@PrimaryGeneratedColumn('uuid', { name: 'comment_flag_id' })` |
| `violation` | Yes | `string` | `@Column({ length: 250 })` |
| `status` | No | `FlagType` | `@Column({ type: 'enum', enum: FlagType })` |
| `userId` | Yes | `string` | `@Column({ name: 'user_id' })` |
| `user` | Yes | `User` | `@ManyToOne(() => User, (user) => user.commentFlags)`<br>`@JoinColumn({ name: 'user_id', referencedColumnName: 'userId' })` |
| `commentId` | Yes | `string` | `@Column({ name: 'comment_id' })` |
| `comment` | Yes | `Comment` | `@ManyToOne(() => Comment, (comment) => comment.flags)`<br>`@JoinColumn({ name: 'comment_id', referencedColumnName: 'commentId' })` |
| `createdAt` | Yes | `Date` | `@CreateDateColumn({ name: 'created_at' })` |
| `updatedAt` | Yes | `Date` | `@UpdateDateColumn({ name: 'updated_at' })` |
| `deletedAt` | Yes | `Date` | `@DeleteDateColumn({ name: 'deleted_at' })` |

## class CommentFlagBodyDto

- Source: `src/agent/dto/social-engagement.dto.ts:35`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `violation` | Yes | `string` | `@IsString`<br>`@MaxLength(250)` |

## class CommentFlagDTO

- Source: `src/activity/dto/commentFlag.dto.ts:5`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `commentFlagId` | Yes | `string` |  |
| `violation` | Yes | `string` |  |
| `userId` | Yes | `string` |  |
| `user` | Yes | `PublicUser` |  |

## class CommentReponseWithTotalDTO

- Source: `src/activity/dto/commentResponseWithTotal.dto.ts:4`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `comments` | Yes | `CommentDTO[]` |  |
| `total` | Yes | `number` |  |
| `totalAll` | Yes | `number` |  |

## class CommentsQueryDto

- Source: `src/agent/dto/social-engagement.dto.ts:41`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `first` | No | `number` | `@IsOptional`<br>`@Type(() => Number)`<br>`@IsInt`<br>`@Min(1)`<br>`@Max(50)` |
| `after` | No | `string` | `@IsOptional`<br>`@IsString` |
| `parent_id` | No | `string` | `@IsOptional`<br>`@IsUUID` |

## class CommentVote

- Source: `src/activity/entities/commentVote.entity.ts:17`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `commentVoteId` | Yes | `string` | `@PrimaryGeneratedColumn('uuid', { name: 'comment_vote_id' })` |
| `userId` | Yes | `string` | `@Column({ name: 'user_id' })` |
| `user` | Yes | `User` | `@ManyToOne(() => User, (user) => user.commentVotes)`<br>`@JoinColumn({ name: 'user_id', referencedColumnName: 'userId' })` |
| `commentId` | Yes | `string` | `@Column({ name: 'comment_id' })` |
| `comment` | Yes | `Comment` | `@ManyToOne(() => Comment, (comment) => comment.votes)`<br>`@JoinColumn({ name: 'comment_id', referencedColumnName: 'commentId' })` |
| `vote` | Yes | `VoteType` | `@Column({ type: 'enum', enum: VoteType })` |
| `createdAt` | Yes | `Date` | `@CreateDateColumn({ name: 'created_at' })` |
| `updatedAt` | Yes | `Date` | `@UpdateDateColumn({ name: 'updated_at' })` |

## class CommentVoteBodyDto

- Source: `src/agent/dto/social-engagement.dto.ts:30`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `vote` | Yes | `VoteType` | `@IsEnum(VoteType)` |

## class CommunityDTO

- Source: `src/listing/dto/community.dto.ts:3`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `name` | Yes | `string` |  |
| `description` | Yes | `string` |  |
| `website` | Yes | `string` |  |
| `discord` | Yes | `string` |  |
| `twitter` | Yes | `string` |  |
| `instagram` | Yes | `string` |  |
| `tiktok` | Yes | `string` |  |
| `telegram` | Yes | `string` |  |

## class CompletePayPalSetupDto

- Source: `src/agent/dto/setup-paypal.dto.ts:11`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `setup_token_id` | Yes | `string` | `@IsString`<br>`@IsNotEmpty` |

## class Config

- Source: `src/config/entities/config.entity.ts:12`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `configId` | Yes | `number` | `@PrimaryGeneratedColumn({ name: 'config_id' })` |
| `key` | Yes | `string` | `@Column('character varying', { name: 'key' })` |
| `name` | Yes | `string` | `@Column('character varying', { name: 'name' })` |
| `description` | Yes | `string` | `@Column('character varying', { name: 'description', default: null })` |
| `value` | Yes | `string` | `@Column('character varying', { name: 'value', default: null })` |
| `category` | Yes | `string` | `@Column('character varying', { name: 'category', default: null })` |
| `createdAt` | Yes | `Date` | `@CreateDateColumn({ name: 'created_at' })` |
| `updatedAt` | Yes | `Date` | `@UpdateDateColumn({ name: 'updated_at' })` |
| `deletedAt` | Yes | `Date` | `@DeleteDateColumn({ name: 'deleted_at' })` |

## enum CONFIG_KEYS

- Source: `src/utils/types.ts:13`

| Member | Value |
|---|---|
| `PAID_SHARE_TIMEOUT_PER_USER` | `'PAID_SHARE_TIMEOUT_PER_USER'` |
| `PAID_SHARE_MAX_PER_USER` | `'PAID_SHARE_MAX_PER_USER'` |
| `SHARE_TIMEOUT_PER_USER` | `'SHARE_TIMEOUT_PER_USER'` |
| `TOKEN_RESERVE_SUPPLY` | `'TOKEN_RESERVE_SUPPLY'` |
| `TOKEN_TOTAL_SUPPLY` | `'TOKEN_TOTAL_SUPPLY'` |
| `POINT_BASE_RATE` | `'POINT_BASE_RATE'` |
| `NSFW_SCORE` | `'NSFW_SCORE'` |
| `ERC20_ADD_TOKEN_PRICE` | `'ERC20_ADD_TOKEN_PRICE'` |
| `PLATFORM_COMMISSION` | `'PLATFORM_COMMISSION'` |
| `DOWNLOAD_COMMISSION_RATE` | `'DOWNLOAD_COMMISSION_RATE'` |
| `DOWNLOAD_FIXED_FEE` | `'DOWNLOAD_FIXED_FEE'` |
| `OWNERSHIP_COMMISSION_RATE` | `'OWNERSHIP_COMMISSION_RATE'` |
| `OWNERSHIP_FIXED_FEE` | `'OWNERSHIP_FIXED_FEE'` |
| `SELLER_COMMISSION` | `'SELLER_COMMISSION'` |
| `ARTIST_COMMISSION` | `'ARTIST_COMMISSION'` |
| `MNEMONIC` | `'MNEMONIC'` |
| `AUTO_APPROVAL_CREATOR_BASED_FOLLOWERS` | `'AUTO_APPROVAL_CREATOR_BASED_FOLLOWERS'` |
| `REJECTION_MESSAGE` | `'REJECTION_MESSAGE'` |
| `MAX_DIRECT_SIGNUP_LIMIT` | `'MAX_DIRECT_SIGNUP_LIMIT'` |
| `INVITE_LIMIT_FREE` | `'INVITE_LIMIT_FREE'` |
| `INVITE_LIMIT_SUBSCRIBED` | `'INVITE_LIMIT_SUBSCRIBED'` |
| `ENABLE_MULTIPLE_ASSET` | `'ENABLE_MULTIPLE_ASSET'` |
| `POINTS_REDEEM_THRESHOLD` | `'POINTS_REDEEM_THRESHOLD'` |
| `NSFW_LIKELY_SCORE` | `'NSFW_LIKELY_SCORE'` |
| `QC_MIN_ENTROPY` | `'QC_MIN_ENTROPY'` |
| `QC_MIN_SHARPNESS` | `'QC_MIN_SHARPNESS'` |
| `QC_IMAGE_MIN_WIDTH` | `'QC_IMAGE_MIN_WIDTH'` |
| `QC_IMAGE_MIN_HEIGHT` | `'QC_IMAGE_MIN_HEIGHT'` |
| `QC_VIDEO_MIN_WIDTH` | `'QC_VIDEO_MIN_WIDTH'` |
| `QC_VIDEO_MIN_HEIGHT` | `'QC_VIDEO_MIN_HEIGHT'` |
| `DEDUPE_IMAGE_HAMMING_THRESHOLD` | `'DEDUPE_IMAGE_HAMMING_THRESHOLD'` |
| `DEDUPE_ASPECT_RATIO_TOLERANCE` | `'DEDUPE_ASPECT_RATIO_TOLERANCE'` |
| `DEDUPE_CONTENT_LENGTH_TOLERANCE` | `'DEDUPE_CONTENT_LENGTH_TOLERANCE'` |
| `DEDUPE_VIDEO_SIMILARITY_THRESHOLD` | `'DEDUPE_VIDEO_SIMILARITY_THRESHOLD'` |
| `DEDUPE_AUDIO_SIMILARITY_THRESHOLD` | `'DEDUPE_AUDIO_SIMILARITY_THRESHOLD'` |

## class ConfigValueDTO

- Source: `src/config/dto/configValue.dto.ts:4`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `key` | Yes | `string` | `@IsString` |
| `value` | Yes | `string` | `@IsString` |

## class ConfirmOwnershipPurchaseDTO

- Source: `src/paypal/dto/confirmOwnershipPurchase.dto.ts:3`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `listingId` | Yes | `string` |  |
| `orderId` | Yes | `string` |  |

## class ConfirmOwnershipPurchaseResponseDTO

- Source: `src/paypal/dto/confirmOwnershipPurchaseResponse.dto.ts:3`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `success` | Yes | `boolean` |  |
| `transactionId` | No | `string` |  |

## class ContractType

- Source: `src/listing/entities/contractType.entity.ts:13`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `contractTypeId` | Yes | `number` | `@PrimaryGeneratedColumn({ name: 'contract_type_id' })` |
| `name` | Yes | `string` | `@Column('character varying', { name: 'name' })` |
| `allowCommercialUse` | Yes | `boolean` | `@Column({ name: 'allow_commercial_use', default: false })` |
| `allowModifications` | Yes | `boolean` | `@Column({ name: 'allow_modifications', default: false })` |
| `attributionRequired` | Yes | `boolean` | `@Column({ name: 'attribution_required', default: true })` |
| `exclusivity` | Yes | `string` | `@Column('character varying', { name: 'exclusivity', default: 'non_exclusive', })` |
| `listings` | Yes | `Listing[]` | `@OneToMany(() => Listing, (listing) => listing.contractType)` |
| `createdAt` | Yes | `Date` | `@CreateDateColumn({ name: 'created_at' })` |
| `updatedAt` | Yes | `Date` | `@UpdateDateColumn({ name: 'updated_at' })` |
| `deletedAt` | Yes | `Date` | `@DeleteDateColumn({ name: 'deleted_at' })` |

## enum CounterEntity

- Source: `src/counter/counter.types.ts:1`

| Member | Value |
|---|---|
| `LISTING` | `'listing'` |
| `FOLDER` | `'folder'` |

## class CounterOfferDto
_Unix timestamp (seconds), defaults to 7 days if omitted_

- Source: `src/agent/dto/offer.dto.ts:30`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `counter_price` | Yes | `number` | `@IsNumber`<br>`@Min(2)` |
| `deadline` | No | `number` | `@IsNumber`<br>`@IsOptional` |

## class CounterOfferInputDTO

- Source: `src/marketplace/dto/counter-offer-input.dto.ts:4`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `offerId` | Yes | `string` | `@IsUUID` |
| `counterPrice` | Yes | `number` | `@IsNumber`<br>`@Min(2)` |
| `deadline` | No | `number` | `@IsOptional`<br>`@IsNumber` |

## class CreateAgentListingDto

- Source: `src/agent/dto/create-listing.dto.ts:19`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `name` | Yes | `string` | `@IsString`<br>`@IsNotEmpty`<br>`@MaxLength(50)` |
| `description` | Yes | `string` | `@IsString`<br>`@IsNotEmpty`<br>`@MaxLength(5000)` |
| `price` | No | `number` | `@IsOptional`<br>`@IsNumber`<br>`@Min(0)`<br>`@Type(() => Number)` |
| `tags` | No | `string[]` | `@IsOptional`<br>`@IsArray`<br>`@IsString({ each: true })`<br>`@ArrayMaxSize(20)` |
| `private` | No | `boolean` | `@IsOptional`<br>`@IsBoolean` |
| `category` | No | `string` | `@IsOptional`<br>`@IsString` |
| `subcategories` | Yes | `string[]` | `@IsArray`<br>`@IsString({ each: true })`<br>`@ArrayMinSize(1)`<br>`@ArrayMaxSize(5)` |
| `contract_type` | Yes | `string` | `@IsString({ message: "contract_type is required and must be a string. Allowed values: 'public_domain', 'non_exclusive'.", })`<br>`@IsNotEmpty({ message: "contract_type is required and cannot be empty. Allowed values: 'public_domain', 'non_exclusive'.", })`<br>`@IsIn(['public_domain', 'non_exclusive'], { message: "contract_type must be 'public_domain' or 'non_exclusive'. The 'exclusive' license is not currently accepted.", })` |
| `model` | No | `string` | `@IsOptional`<br>`@IsString` |
| `prompt` | No | `string` | `@IsOptional`<br>`@IsString` |
| `acknowledge_review` | No | `boolean` | `@IsOptional`<br>`@IsBoolean` |
| `thumbnail_name` | No | `string` | `@IsOptional`<br>`@IsString`<br>`@Matches(/^[a-zA-Z0-9][a-zA-Z0-9._-]*$/, { message: 'Invalid thumbnail filename', })` |
| `file_name` | Yes | `string` | `@IsString`<br>`@IsNotEmpty`<br>`@Matches(/^[a-zA-Z0-9][a-zA-Z0-9._-]*$/, { message: 'Invalid filename' })` |

## class CreateAiModelDTO

- Source: `src/ai-model/dto/createAiModel.dto.ts:3`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `name` | Yes | `string` |  |
| `categoryIds` | Yes | `number[]` |  |
| `sortOrder` | No | `number` |  |

## class CreateAppealDto

- Source: `src/agent/dto/appeal.dto.ts:3`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `reason` | Yes | `string` | `@IsString`<br>`@IsNotEmpty`<br>`@MaxLength(1000)` |

## class CreateCategoryDTO

- Source: `src/listing/dto/createCategory.dto.ts:4`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `categoryId` | No | `number` | `@IsNumber`<br>`@IsOptional` |
| `type` | Yes | `string` | `@IsOptional`<br>`@IsString` |
| `icon` | No | `string` | `@IsOptional`<br>`@IsString` |
| `smallIcon` | No | `string` | `@IsOptional`<br>`@IsString` |
| `label` | No | `string` | `@IsOptional`<br>`@IsString` |
| `parentId` | No | `number` | `@IsNumber`<br>`@IsOptional` |

## class CreateCommunityDTO

- Source: `src/listing/dto/createCommunity.dto.ts:3`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `name` | Yes | `string` |  |
| `description` | Yes | `string` |  |
| `website` | Yes | `string` |  |
| `discord` | Yes | `string` |  |
| `twitter` | Yes | `string` |  |
| `instagram` | Yes | `string` |  |
| `tiktok` | Yes | `string` |  |
| `telegram` | Yes | `string` |  |

## class CreateFolderInput

- Source: `src/folder/dto/create-folder.dto.ts:12`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `name` | Yes | `string` | `@IsString`<br>`@MaxLength(100)` |
| `type` | Yes | `FolderType` | `@IsEnum(FolderType)` |
| `visibility` | No | `FolderVisibility` | `@IsEnum(FolderVisibility)`<br>`@IsOptional` |
| `thumbnailUrl` | No | `string` | `@IsString`<br>`@MaxLength(2048)`<br>`@IsOptional` |
| `description` | No | `string` | `@IsString`<br>`@MaxLength(1000)`<br>`@IsOptional` |
| `tags` | No | `string[]` | `@IsArray`<br>`@ArrayMaxSize(20)`<br>`@IsString({ each: true })`<br>`@MaxLength(32, { each: true })`<br>`@IsOptional` |

## class CreateNotificationDto

- Source: `src/notifications/dto/createNotification.dto.ts:4`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `notificationId` | No | `string` | `@IsOptional` |
| `id` | Yes | `string` | `@IsEmail` |
| `title` | Yes | `string` | `@IsString`<br>`@Max(250)` |
| `link` | Yes | `string` | `@IsString` |
| `message` | Yes | `string` | `@IsString`<br>`@Max(1000)` |

## class CreateOfferDto
_Unix timestamp (seconds) for offer deadline_

- Source: `src/agent/dto/offer.dto.ts:12`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `listing_id` | Yes | `string` | `@IsUUID` |
| `price` | Yes | `number` | `@IsNumber`<br>`@Min(2)` |
| `deadline` | Yes | `number` | `@IsNumber` |
| `payment_id` | No | `string` | `@IsString`<br>`@IsOptional` |

## class CreateOfferInputDTO

- Source: `src/marketplace/dto/offerCreatedInput.dto.ts:4`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `listingId` | Yes | `string` | `@IsString` |
| `price` | Yes | `number` | `@IsNumber` |
| `deadline` | Yes | `number` | `@IsNumber` |
| `paymentId` | No | `string` | `@IsString`<br>`@IsOptional` |

## class CreatePayTokenDTO

- Source: `src/listing/dto/createPayToken.dto.ts:5`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `payTokenId` | Yes | `number` | `@IsOptional` |
| `assetId` | Yes | `string` | `@IsOptional`<br>`@IsUUID` |
| `name` | Yes | `string` | `@IsOptional` |
| `symbol` | Yes | `string` | `@IsOptional` |
| `address` | Yes | `string` | `@IsOptional`<br>`@IsEthereumAddress` |
| `chainlinkProxyAddress` | Yes | `string` | `@IsOptional` |
| `decimals` | Yes | `number` | `@IsOptional` |
| `isMainnet` | Yes | `boolean` | `@IsOptional` |
| `isDisabled` | Yes | `boolean` | `@IsOptional` |
| `community` | Yes | `CreateCommunityDTO` | `@IsOptional` |

## class CreateQADTO

- Source: `src/user/dto/createQA.dto.ts:4`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `qaId` | No | `number` | `@IsOptional`<br>`@IsNumber` |
| `question` | Yes | `string` | `@IsString` |
| `answer` | Yes | `string` | `@IsString` |
| `questionTypeId` | Yes | `number` | `@IsNumber` |

## class CreateQuestionTypeDTO

- Source: `src/user/dto/createQuestionType.dto.ts:4`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `questionTypeId` | No | `number` | `@IsOptional`<br>`@IsNumber` |
| `type` | Yes | `string` | `@IsString` |

## class CreateUploadPresignedUrlDTO

- Source: `src/listing/dto/createUploadPresignedUrl.dto.ts:4`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `fileName` | Yes | `string` | `@IsString` |
| `assetType` | Yes | `string` | `@IsString` |
| `parentId` | No | `string` | `@IsOptional`<br>`@IsUUID` |
| `fileSize` | No | `number` | `@IsOptional`<br>`@IsNumber`<br>`@Min(1)` |
| `listingId` | Yes | `string` | `@IsUUID` |

## class CreateUploadPresignedUrlResponseDTO

- Source: `src/listing/dto/createUploadPresignedUrlResponse.dto.ts:5`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `asset` | Yes | `Asset` |  |
| `responsePutSignedUrl` | Yes | `string` | `@IsString` |
| `responseGetUrl` | Yes | `string` | `@IsString` |
| `shortUrl` | Yes | `string` | `@IsString` |

## class CreateUserPresignedUrlDTO

- Source: `src/user/dto/createUserPresignedUrl.dto.ts:4`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `fileName` | Yes | `string` | `@IsString` |
| `type` | Yes | `'banner' \| 'avatar' \| 'folder-thumbnail'` | `@IsString` |
| `contentType` | No | `string` | `@IsOptional`<br>`@IsString`<br>`@Matches(/^image\/(png\|jpeg\|gif\|webp\|avif\|bmp)$/)` |

## class CreateUserPresignedUrlResponseDTO

- Source: `src/user/dto/createUserPresignedUrlResponse.dto.ts:4`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `responsePutSignedUrl` | Yes | `string` | `@IsString` |
| `responseGetUrl` | Yes | `string` | `@IsString` |

## class CreatorAnalyticsDTO

- Source: `src/analytics/dto/creator-analytics.dto.ts:3`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `userId` | Yes | `string` |  |
| `totalListings` | Yes | `number` |  |
| `totalSales` | Yes | `number` |  |
| `totalRevenue` | Yes | `number` |  |
| `followerCount` | Yes | `number` |  |

## class CreatorStatus

- Source: `src/user/entities/creatorStatus.entity.ts:14`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `creatorStatusId` | Yes | `number` | `@PrimaryGeneratedColumn({ name: 'creator_status_id' })` |
| `name` | Yes | `string` | `@Column('character varying', { name: 'name' })` |
| `users` | Yes | `User[]` | `@OneToMany(() => User, (users) => users.creatorStatus)` |
| `createdAt` | Yes | `Date` | `@CreateDateColumn({ name: 'created_at' })` |
| `updatedAt` | Yes | `Date` | `@UpdateDateColumn({ name: 'updated_at' })` |
| `deletedAt` | Yes | `Date` | `@DeleteDateColumn({ name: 'deleted_at' })` |

## class CreatorStatusDTO

- Source: `src/user/dto/creatorStatus.dto.ts:4`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `creatorStatusId` | No | `number` | `@IsNumber` |
| `message` | Yes | `string` | `@IsString` |

## type CreatorStatusType

- Source: `src/utils/types.ts:3`
- Type: `'approved' \| 'paused' \| 'rejected'`

## class CreditBalanceDTO

- Source: `src/billing/dto/billing.dto.ts:65`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `subscriptionCredits` | Yes | `number` |  |
| `topupCredits` | Yes | `number` |  |
| `totalCredits` | Yes | `number` |  |
| `topupExpiresAt` | Yes | `Date \| null` |  |
| `tier` | Yes | `string` |  |
| `overage` | Yes | `OverageDTO \| null` |  |

## class CreditHistoryQueryDto

- Source: `src/agent/dto/account.dto.ts:13`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `limit` | No | `number` | `@IsOptional`<br>`@Type(() => Number)`<br>`@IsInt`<br>`@Min(1)`<br>`@Max(100)` |
| `offset` | No | `number` | `@IsOptional`<br>`@Type(() => Number)`<br>`@IsInt`<br>`@Min(0)` |

## class CreditLedger

- Source: `src/billing/entities/credit-ledger.entity.ts:20`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `id` | Yes | `string` | `@PrimaryGeneratedColumn('uuid', { name: 'id' })` |
| `userId` | Yes | `string` | `@Column({ name: 'user_id', type: 'uuid' })` |
| `amount` | Yes | `number` | `@Column({ name: 'amount', type: 'int' })` |
| `type` | Yes | `CreditLedgerType` | `@Column({ name: 'type', type: 'enum', enum: CreditLedgerType })` |
| `endpoint` | No | `string` | `@Column({ name: 'endpoint', nullable: true })` |
| `referenceId` | No | `string` | `@Column({ name: 'reference_id', nullable: true })` |
| `createdAt` | Yes | `Date` | `@CreateDateColumn({ name: 'created_at' })` |

## class CreditLedgerDTO

- Source: `src/billing/dto/billing.dto.ts:86`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `id` | Yes | `string` |  |
| `amount` | Yes | `number` |  |
| `type` | Yes | `string` |  |
| `endpoint` | No | `string` |  |
| `createdAt` | Yes | `Date` |  |

## enum CreditLedgerType

- Source: `src/billing/entities/credit-ledger.entity.ts:10`

| Member | Value |
|---|---|
| `MONTHLY_GRANT` | `'monthly_grant'` |
| `ADMIN_GRANT` | `'admin_grant'` |
| `TOP_UP` | `'top_up'` |
| `USAGE` | `'usage'` |
| `REFUND` | `'refund'` |
| `STARTER_GRANT` | `'starter_grant'` |
| `EXPIRY` | `'expiry'` |

## class CreditTopUp

- Source: `src/billing/entities/credit-top-up.entity.ts:39`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `id` | Yes | `string` | `@PrimaryGeneratedColumn('uuid', { name: 'id' })` |
| `userId` | Yes | `string` | `@Column({ name: 'user_id', type: 'uuid' })` |
| `tier` | Yes | `TopUpTier` | `@Column({ name: 'tier', type: 'enum', enum: TopUpTier })` |
| `triggerThreshold` | Yes | `number` | `@Column({ name: 'trigger_threshold', type: 'int' })` |
| `creditsPerCharge` | Yes | `number` | `@Column({ name: 'credits_per_charge', type: 'int' })` |
| `priceCents` | Yes | `number` | `@Column({ name: 'price_cents', type: 'int' })` |
| `active` | Yes | `boolean` | `@Column({ name: 'active', type: 'boolean', default: true })` |
| `lastTriggeredAt` | No | `Date` | `@Column({ name: 'last_triggered_at', type: 'timestamptz', nullable: true })` |
| `createdAt` | Yes | `Date` | `@CreateDateColumn({ name: 'created_at' })` |

## class CreditTopUpDto

- Source: `src/agent/dto/account.dto.ts:64`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `tier` | Yes | `string` | `@Transform(({ value }) => value?.toLowerCase())`<br>`@IsIn(['starter', 'basic', 'plus', 'power'])` |

## class CreditWallet

- Source: `src/billing/entities/credit-wallet.entity.ts:13`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `id` | Yes | `string` | `@PrimaryGeneratedColumn('uuid', { name: 'id' })` |
| `userId` | Yes | `string` | `@Column({ name: 'user_id' })` |
| `walletType` | Yes | `WalletType` | `@Column({ name: 'wallet_type', type: 'varchar', length: 20 })` |
| `balance` | Yes | `number` | `@Column({ name: 'balance', type: 'int', default: 0 })` |
| `expiresAt` | Yes | `Date \| null` | `@Column({ name: 'expires_at', type: 'timestamptz', nullable: true })` |
| `createdAt` | Yes | `Date` | `@CreateDateColumn({ name: 'created_at', type: 'timestamptz' })` |
| `updatedAt` | Yes | `Date` | `@UpdateDateColumn({ name: 'updated_at', type: 'timestamptz' })` |

## class CursorLimitQueryDto

- Source: `src/agent/dto/analytics-query.dto.ts:16`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `cursor` | No | `string` | `@IsOptional`<br>`@IsString` |
| `limit` | No | `number` | `@IsOptional`<br>`@Type(() => Number)`<br>`@IsInt`<br>`@Min(1)`<br>`@Max(50)` |

## interface CustomExceptionOptions
_Server-known dynamic state to include in the error response alongside the static message and recovery hint (e.g. `{plan, limit, current_status}`). Runs through `sanitizeDetails` at construction — values must be primitives or arrays of primitives, keys must be snake_case, and credential-shaped keys (`password`, `token`, ...) are dropped. Do NOT pass user input._

- Source: `src/utils/customException.ts:137`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `details` | No | `Record<string, unknown>` |  |

## class CustomMessageDTO

- Source: `src/utils/generalGraphqlModel.dto.ts:51`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `message` | Yes | `string` |  |

## type DeadLetterHandler

- Source: `src/resilience/outbox/outbox.types.ts:14`
- Type: `( payload: Record<string, any>, idempotencyKey: string, ) => Promise<void>`

## interface DeductResult

- Source: `src/billing/wallet.service.ts:12`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `success` | Yes | `boolean` |  |
| `totalRemaining` | Yes | `number` |  |
| `subscriptionRemaining` | Yes | `number` |  |
| `topupRemaining` | Yes | `number` |  |
| `effectiveTier` | Yes | `string` |  |

## interface DeviceFlowResponse

- Source: `src/agent/dto/device-flow.dto.ts:17`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `status` | Yes | `'pending_confirmation'` |  |
| `message` | Yes | `string` |  |
| `device_code` | Yes | `string` |  |
| `user_code` | Yes | `string` |  |
| `verification_uri` | Yes | `string` |  |
| `verification_uri_complete` | Yes | `string` |  |
| `expires_in` | Yes | `number` |  |
| `interval` | Yes | `number` |  |

## class DeviceInfoQueryDto

- Source: `src/agent/dto/device-flow.dto.ts:9`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `user_code` | Yes | `string` | `@IsNotEmpty`<br>`@IsString` |

## interface DeviceInfoResponse

- Source: `src/agent/dto/device-flow.dto.ts:40`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `user_code` | Yes | `string` |  |
| `agent_name` | Yes | `string` |  |
| `callback_url` | Yes | `string \| null` |  |
| `description` | Yes | `string \| null` |  |

## interface DeviceOwnershipOptions

- Source: `src/auth/plugins/device-ownership.plugin.ts:12`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `valkey` | Yes | `ValkeyLike` |  |

## class DeviceStatusQueryDto

- Source: `src/agent/dto/device-flow.dto.ts:3`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `device_code` | Yes | `string` | `@IsNotEmpty`<br>`@IsString` |

## interface DeviceStatusResponse
_Present only when status === 'confirmed'_

- Source: `src/agent/dto/device-flow.dto.ts:28`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `status` | Yes | `'pending' \| 'confirmed' \| 'denied' \| 'expired'` |  |
| `agent_id` | No | `string` |  |
| `api_key` | No | `string` |  |
| `interval` | No | `number` |  |
| `message` | No | `string` |  |

## class Download

- Source: `src/listing/entities/download.entity.ts:15`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `downloadId` | Yes | `string` | `@PrimaryGeneratedColumn('uuid', { name: 'download_id' })` |
| `listingId` | Yes | `string` | `@Column({ name: 'listing_id' })` |
| `listing` | Yes | `Listing` | `@ManyToOne(() => Listing, (listing) => listing.downloads)`<br>`@JoinColumn({ name: 'listing_id', referencedColumnName: 'listingId' })` |
| `userId` | Yes | `string` | `@Column({ name: 'user_id' })` |
| `user` | Yes | `User` | `@ManyToOne(() => User, (user) => user.downloads)`<br>`@JoinColumn({ name: 'user_id', referencedColumnName: 'userId' })` |
| `createdAt` | Yes | `Date` | `@CreateDateColumn({ name: 'created_at' })` |

## type DurationUnit

- Source: `src/utils/time.ts:3`
- Type: `'seconds' \| 'minutes' \| 'hours' \| 'days' \| 'weeks' \| 'months' \| 'years'`

## class EmailChangeDto

- Source: `src/agent/dto/email-change.dto.ts:5`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `new_email` | Yes | `string` | `@IsEmail`<br>`@Transform(({ value }) => value?.toLowerCase().trim())` |
| `password` | Yes | `string` | `@IsString`<br>`@MinLength(PASSWORD_RULES.minLength)`<br>`@MaxLength(PASSWORD_RULES.maxLength)` |

## interface EmailPayload

- Source: `src/notifications/types/payloads.ts:1`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `subject` | Yes | `string` |  |
| `content` | Yes | `string` |  |
| `content2` | No | `string` |  |
| `content3` | No | `string` |  |
| `warning` | No | `string` |  |
| `code` | No | `string` |  |
| `link` | Yes | `string` |  |
| `button` | Yes | `string` |  |

## interface EmailProvider

- Source: `src/notifications/providers/email-provider.interface.ts:5`

_No declared properties._

## class EndpointCreditCost

- Source: `src/billing/entities/endpoint-credit-cost.entity.ts:10`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `id` | Yes | `string` | `@PrimaryGeneratedColumn('uuid', { name: 'id' })` |
| `endpoint` | Yes | `string` | `@Column({ name: 'endpoint', unique: true })` |
| `creditCost` | Yes | `number` | `@Column({ name: 'credit_cost', type: 'int', default: 0 })` |
| `createdAt` | Yes | `Date` | `@CreateDateColumn({ name: 'created_at' })` |
| `updatedAt` | Yes | `Date` | `@UpdateDateColumn({ name: 'updated_at' })` |

## type EngagementKindInput

- Source: `src/folder/services/folder-engagement.service.ts:24`
- Type: `'LIKE' \| 'SAVE' \| 'FOLLOW'`

## type EngagementMutationResult

- Source: `src/folder/services/folder-engagement.service.ts:25`
- Type: `{ changed: boolean }`

## interface EngagementWeights

- Source: `src/viral-score/viral-score.service.ts:13`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `view` | Yes | `number` |  |
| `like` | Yes | `number` |  |
| `favorite` | Yes | `number` |  |
| `share` | Yes | `number` |  |
| `comment` | Yes | `number` |  |
| `download` | Yes | `number` |  |
| `offer` | Yes | `number` |  |
| `sale` | Yes | `number` |  |

## class EstimateQueryDto

- Source: `src/agent/dto/marketplace-purchase.dto.ts:34`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `price` | Yes | `number` | `@IsNumber({ maxDecimalPlaces: 2 })`<br>`@Min(0)`<br>`@Type(() => Number)` |
| `purchase_type` | No | `'download' \| 'ownership'` | `@IsOptional`<br>`@IsIn(['download', 'ownership'])` |

## interface EventData

- Source: `src/chain-call/entities/chainCall.entity.ts:51`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `user` | Yes | `string` |  |
| `contentId` | No | `string` |  |
| `tokenId` | No | `number` |  |
| `price` | No | `number` |  |
| `deadline` | No | `number` |  |

## class EventLedger

- Source: `src/activity/entities/event-ledger.entity.ts:17`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `eventId` | Yes | `string` | `@PrimaryGeneratedColumn('uuid', { name: 'event_id' })` |
| `listingId` | Yes | `string` | `@Column({ name: 'listing_id', nullable: true })` |
| `listing` | Yes | `Listing` | `@ManyToOne(() => Listing, (listing) => listing.eventLedgerEntries)`<br>`@JoinColumn({ name: 'listing_id', referencedColumnName: 'listingId' })` |
| `userId` | Yes | `string` | `@Column({ name: 'user_id', nullable: true })` |
| `user` | Yes | `User` | `@ManyToOne(() => User, (user) => user.eventLedgerEntries)`<br>`@JoinColumn({ name: 'user_id', referencedColumnName: 'userId' })` |
| `eventName` | Yes | `string` | `@Column('character varying', { name: 'event_name', nullable: true })` |
| `eventDetails` | Yes | `Record<string, any>` | `@Column('jsonb', { name: 'event_details', nullable: true })` |
| `txHash` | Yes | `string` | `@Column('character varying', { name: 'tx_hash' })` |
| `createdAt` | Yes | `Date` | `@CreateDateColumn({ name: 'created_at' })` |
| `updatedAt` | Yes | `Date` | `@UpdateDateColumn({ name: 'updated_at' })` |
| `deletedAt` | Yes | `Date` | `@DeleteDateColumn({ name: 'deleted_at' })` |

## interface ExportFailureClassification
_Classify a Bull `job.failedReason` string into an agent-facing fine-grained error code + a recovery hint. Bull retains `failedReason` for 24 hours (matches our `removeOnFail.age` setting) so we don't need a separate table to recover the failure cause on a late poll. The classifier is deliberately string-based because job failures originate from many code paths (BadRequestException thrown in the processor, AWS SDK errors, timeouts from the job runner) — regex lookups are the most robust signal we can rely on post-facto._

- Source: `src/analytics/classify-export-failure.ts:13`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `code` | Yes | `\| 'EXPORT_TIMEOUT' \| 'EXPORT_UPSTREAM' \| 'EXPORT_ROW_LIMIT' \| 'EXPORT_AUTH' \| 'EXPORT_UNKNOWN'` |  |
| `hint` | Yes | `string` |  |

## interface ExtractedErrorBody
_Normalized error body the filter emits to HTTP and summarizes into GraphQLError extensions. All fields beyond `message` / `error` are additive — legacy clients that only read `{statusCode, message, error}` continue to work unchanged._

- Source: `src/utils/global-exception.filter.ts:30`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `message` | Yes | `string` |  |
| `error` | No | `GraphQLErrorCode` |  |
| `code` | No | `string` |  |
| `hint` | No | `string` |  |
| `next` | No | `{ options?: RecoveryOption[]; docs?: string }` |  |
| `fields` | No | `unknown[]` |  |
| `details` | No | `SanitizedDetails` |  |
| `retryAfter` | No | `number` |  |

## type FailureReason

- Source: `src/listing/utils/failureReason.ts:12`
- Type: `(typeof FAILURE_REASONS)[keyof typeof FAILURE_REASONS]`

## class FeatureFlagsDTO

- Source: `src/config/dto/feature-flags.dto.ts:3`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `marketplaceEnabled` | Yes | `boolean` |  |

## enum FeedEventType

- Source: `src/feed/dto/feed.dto.ts:3`

| Member | Value |
|---|---|
| `NEW_LISTING` | `'NEW_LISTING'` |
| `PRICE_CHANGE` | `'PRICE_CHANGE'` |
| `LISTING_SOLD` | `'LISTING_SOLD'` |

## class FeedItemDTO

- Source: `src/feed/dto/feed.dto.ts:11`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `type` | Yes | `FeedEventType` |  |
| `creatorId` | Yes | `string` |  |
| `creatorName` | Yes | `string` |  |
| `listingId` | Yes | `string` |  |
| `listingTitle` | Yes | `string` |  |
| `price` | No | `number` |  |
| `timestamp` | Yes | `Date` |  |

## class FeedResponseDTO

- Source: `src/feed/dto/feed.dto.ts:35`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `items` | Yes | `FeedItemDTO[]` |  |
| `nextCursor` | No | `string` |  |
| `hasMore` | Yes | `boolean` |  |

## type FeedTargetParent

- Source: `src/user-feed-queue/resolvers/feed-target.resolver.ts:11`
- Type: `{ targetType: FeedTargetType; targetId: string; __hydratedTarget?: Folder \| Asset \| null; }`

## enum FeedTargetType

- Source: `src/user-feed-queue/enums/feed-target-type.enum.ts:3`

| Member | Value |
|---|---|
| `FOLDER` | `'FOLDER'` |
| `ASSET` | `'ASSET'` |

## type FeedTargetUnion

- Source: `src/user-feed-queue/dto/feed-target.union.ts:20`
- Type: `Folder \| Asset`

## type FeedTargetUnion

- Source: `src/user-feed-queue/services/feed-target-hydration.service.ts:19`
- Type: `Folder \| Asset`

## class FetchFlaggedListingsDTO

- Source: `src/search/dto/fetch-flagged-listings.dto.ts:4`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `flagFilter` | Yes | `string` | `@IsString` |
| `from` | Yes | `number` | `@IsNumber`<br>`@IsOptional` |
| `count` | Yes | `number` | `@IsNumber`<br>`@Max(100)`<br>`@IsOptional` |

## class FetchListingsCursorDTO

- Source: `src/search/dto/fetch-listings-cursor.dto.ts:12`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `sortby` | Yes | `string` | `@IsString` |
| `first` | Yes | `number` | `@IsNumber`<br>`@Min(1)`<br>`@Max(50)` |
| `after` | No | `string` | `@IsString`<br>`@IsOptional` |
| `searchKey` | No | `string` | `@IsString`<br>`@IsOptional` |
| `userId` | No | `string` | `@IsUUID`<br>`@IsOptional` |
| `contractTypeId` | No | `number` | `@IsNumber`<br>`@IsOptional` |
| `statusIdList` | No | `number[]` | `@IsOptional` |
| `statusFilter` | No | `string[]` | `@IsOptional` |
| `paymentFilter` | No | `string[]` | `@IsOptional` |
| `categoryIdList` | No | `number[]` | `@IsOptional` |
| `categoryType` | No | `string` | `@IsString`<br>`@IsOptional` |
| `priceRangeFrom` | No | `number` | `@IsOptional` |
| `priceRangeTo` | No | `number` | `@IsOptional` |
| `onlyFavorites` | No | `string` | `@IsUUID`<br>`@IsOptional` |
| `onlyLikes` | No | `string` | `@IsUUID`<br>`@IsOptional` |
| `allow` | No | `string` | `@IsOptional` |
| `onlyMinted` | No | `boolean` | `@IsBoolean`<br>`@IsOptional` |
| `exceptListingId` | No | `string` | `@IsUUID`<br>`@IsOptional` |
| `paymentMethod` | No | `string` | `@IsOptional` |
| `followedOnly` | No | `boolean` | `@IsBoolean`<br>`@IsOptional` |
| `includeZip` | No | `boolean` | `@IsBoolean`<br>`@IsOptional` |
| `isPrivate` | No | `boolean` | `@IsBoolean`<br>`@IsOptional` |

## class FetchListingsDTO
_@deprecated Ignored by Typesense search — use searchKey for creator name search_

- Source: `src/listing/dto/fetchListings.dto.ts:11`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `sortby` | Yes | `string` | `@IsString` |
| `from` | Yes | `number` | `@IsNumber` |
| `count` | Yes | `number` | `@IsNumber`<br>`@Max(100)` |
| `searchKey` | Yes | `string` | `@IsString`<br>`@IsOptional` |
| `owner` | Yes | `string` | `@IsString`<br>`@IsOptional` |
| `userId` | Yes | `string` | `@IsUUID`<br>`@IsOptional` |
| `contractTypeId` | Yes | `number` | `@IsNumber`<br>`@IsOptional` |
| `statusIdList` | Yes | `number[]` | `@IsOptional` |
| `statusFilter` | Yes | `string[]` | `@IsOptional` |
| `paymentFilter` | Yes | `string[]` | `@IsOptional` |
| `categoryIdList` | Yes | `number[]` | `@IsOptional` |
| `categoryType` | No | `string` | `@IsString`<br>`@IsOptional` |
| `payTokenIdList` | Yes | `number[]` | `@IsOptional` |
| `communityIdList` | Yes | `number[]` | `@IsOptional` |
| `dateOfCreation` | Yes | `[Date, Date]` | `@IsOptional` |
| `dateOfPurchase` | Yes | `[Date, Date]` | `@IsOptional` |
| `priceRangeFrom` | No | `number` | `@IsOptional` |
| `priceRangeTo` | No | `number` | `@IsOptional` |
| `onlyFavorites` | Yes | `string` | `@IsUUID`<br>`@IsOptional` |
| `onlyLikes` | Yes | `string` | `@IsUUID`<br>`@IsOptional` |
| `allow` | Yes | `string` | `@IsOptional` |
| `flagFilter` | No | `string` | `@IsString`<br>`@IsOptional` |
| `onlyMinted` | No | `boolean` | `@IsBoolean`<br>`@IsOptional` |
| `exceptListingId` | Yes | `string` | `@IsUUID`<br>`@IsOptional` |
| `paymentMethod` | Yes | `string` | `@IsOptional` |
| `followedOnly` | Yes | `boolean` | `@IsBoolean`<br>`@IsOptional` |
| `includeZip` | No | `boolean` | `@IsBoolean`<br>`@IsOptional` |
| `isPrivate` | No | `boolean` | `@IsBoolean`<br>`@IsOptional` |

## class FindNotificationDTO

- Source: `src/notifications/dto/findNofitication.dto.ts:11`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `from` | Yes | `number` | `@IsNumber` |
| `count` | Yes | `number` | `@IsNumber`<br>`@Max(10)` |
| `includeViewed` | No | `boolean` | `@IsBoolean`<br>`@IsOptional` |
| `category` | No | `string` | `@IsString`<br>`@IsIn(['all', 'marketplace', 'social'])`<br>`@IsOptional` |

## enum FlagType

- Source: `src/utils/types.ts:54`

| Member | Value |
|---|---|
| `PENDING` | `'pending'` |
| `RESOLVED` | `'resolved'` |

## interface FlushResult

- Source: `src/counter/counter.service.ts:4`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `listing` | Yes | `Map<string, Record<string, number>>` |  |
| `folder` | Yes | `Map<string, Record<string, number>>` |  |
| `dirtyUserIds` | Yes | `string[]` |  |
| `dirtyListingIds` | Yes | `string[]` |  |
| `dirtyFolderIds` | Yes | `string[]` |  |

## class Folder

- Source: `src/folder/entities/folder.entity.ts:65`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `id` | Yes | `string` | `@PrimaryColumn({ type: 'uuid', name: 'id' })` |
| `ownerId` | Yes | `string` | `@Column({ type: 'uuid', name: 'owner_id' })` |
| `owner` | Yes | `User` | `@ManyToOne(() => User)`<br>`@JoinColumn({ name: 'owner_id', referencedColumnName: 'userId' })` |
| `ownerUserName` | No | `string \| null` |  |
| `type` | Yes | `FolderType` | `@Column({ type: 'enum', enum: FolderType, name: 'type' })` |
| `name` | Yes | `string` | `@Column({ type: 'text', name: 'name' })` |
| `visibility` | Yes | `FolderVisibility` | `@Column({ type: 'enum', enum: FolderVisibility, name: 'visibility', default: FolderVisibility.PUBLIC, })` |
| `thumbnailUrl` | Yes | `string \| null` | `@Column({ type: 'text', name: 'thumbnail_url', nullable: true })` |
| `effectiveThumbnailUrl` | No | `string \| null` |  |
| `systemKey` | Yes | `string \| null` | `@Column({ type: 'text', name: 'system_key', nullable: true })` |
| `rank` | Yes | `string \| null` | `@Column({ type: 'text', name: 'rank', nullable: true })` |
| `createdAt` | Yes | `Date` | `@CreateDateColumn({ name: 'created_at' })` |
| `updatedAt` | Yes | `Date` | `@UpdateDateColumn({ name: 'updated_at' })` |
| `description` | Yes | `string \| null` | `@Column({ type: 'text', name: 'description', nullable: true })` |
| `tags` | Yes | `string[] \| null` | `@Column({ type: 'jsonb', name: 'tags', nullable: true })` |
| `likeCount` | Yes | `number` | `@Column({ name: 'like_count', type: 'bigint', default: 0, transformer: bigintToNumber, })` |
| `saveCount` | Yes | `number` | `@Column({ name: 'save_count', type: 'bigint', default: 0, transformer: bigintToNumber, })` |
| `followCount` | Yes | `number` | `@Column({ name: 'follow_count', type: 'bigint', default: 0, transformer: bigintToNumber, })` |
| `viralScore` | Yes | `number \| null` | `@Column({ name: 'viral_score', type: 'float', nullable: true, default: 0 })` |
| `viralScoreUpdatedAt` | Yes | `Date \| null` | `@Column({ name: 'viral_score_updated_at', type: 'timestamptz', nullable: true, })` |
| `listingCount` | Yes | `number` | `@Column({ name: 'listing_count', type: 'bigint', default: 0, transformer: bigintToNumber, })` |
| `totalLikes` | Yes | `number` | `@Column({ name: 'total_likes', type: 'bigint', default: 0, transformer: bigintToNumber, })` |
| `totalViews` | Yes | `number` | `@Column({ name: 'total_views', type: 'bigint', default: 0, transformer: bigintToNumber, })` |
| `priceMin` | Yes | `number \| null` | `@Column({ name: 'price_min', type: 'numeric', precision: 12, scale: 2, nullable: true, transformer: numericToNumber, })` |
| `priceMax` | Yes | `number \| null` | `@Column({ name: 'price_max', type: 'numeric', precision: 12, scale: 2, nullable: true, transformer: numericToNumber, })` |
| `mediaTypes` | Yes | `string[] \| null` | `@Column({ type: 'jsonb', name: 'media_types', nullable: true })` |
| `childLastUpdatedAt` | Yes | `Date \| null` | `@Column({ name: 'child_last_updated_at', type: 'timestamptz', nullable: true, })` |

## enum FolderCounter

- Source: `src/counter/counter.types.ts:26`

| Member | Value |
|---|---|
| `LIKE` | `'likeCount'` |
| `SAVE` | `'saveCount'` |
| `FOLLOW` | `'followCount'` |

## class FolderEngagement

- Source: `src/folder/entities/folder-engagement.entity.ts:25`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `id` | Yes | `string` | `@PrimaryColumn({ type: 'uuid', name: 'id' })` |
| `folderId` | Yes | `string` | `@Column({ type: 'uuid', name: 'folder_id' })` |
| `folder` | Yes | `Folder` | `@ManyToOne(() => Folder, { onDelete: 'CASCADE' })`<br>`@JoinColumn({ name: 'folder_id' })` |
| `userId` | Yes | `string` | `@Column({ type: 'uuid', name: 'user_id' })` |
| `user` | Yes | `User` | `@ManyToOne(() => User, { onDelete: 'CASCADE' })`<br>`@JoinColumn({ name: 'user_id', referencedColumnName: 'userId' })` |
| `kind` | Yes | `FolderEngagementKind` | `@Column({ type: 'enum', enum: FolderEngagementKind, enumName: 'folder_engagement_kind', })` |
| `createdAt` | Yes | `Date` | `@CreateDateColumn({ name: 'created_at' })` |
| `deletedAt` | Yes | `Date \| null` | `@DeleteDateColumn({ name: 'deleted_at' })` |

## enum FolderEngagementKind

- Source: `src/folder/entities/folder-engagement.entity.ts:17`

| Member | Value |
|---|---|
| `LIKE` | `'LIKE'` |
| `SAVE` | `'SAVE'` |
| `FOLLOW` | `'FOLLOW'` |

## class FolderEngagementState
_GraphQL object type returned by the myFolderEngagement query. Reports whether the current user has an ACTIVE engagement row (deleted_at IS NULL) of each kind on a specific folder. Used by the frontend to render the Liked / Save / Follow toggle state on folder detail pages._

- Source: `src/folder/dto/folder-engagement-state.dto.ts:11`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `liked` | Yes | `boolean` |  |
| `saved` | Yes | `boolean` |  |
| `followed` | Yes | `boolean` |  |

## type FolderEventType

- Source: `src/search/folder-search-sync.subscriber.ts:21`
- Type: `'folder.sync' \| 'folder.delete'`

## class FolderListing

- Source: `src/folder/entities/folder-listing.entity.ts:15`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `folderId` | Yes | `string` | `@PrimaryColumn({ type: 'uuid', name: 'folder_id' })` |
| `listingId` | Yes | `string` | `@PrimaryColumn({ type: 'uuid', name: 'listing_id' })` |
| `folderType` | Yes | `FolderType` | `@Column({ type: 'enum', enum: FolderType, name: 'folder_type' })` |
| `rank` | Yes | `string` | `@Column({ type: 'text', name: 'rank' })` |
| `addedAt` | Yes | `Date` | `@CreateDateColumn({ name: 'added_at' })` |
| `updatedAt` | Yes | `Date` | `@UpdateDateColumn({ name: 'updated_at' })` |
| `folder` | Yes | `Folder` | `@ManyToOne(() => Folder, { onDelete: 'CASCADE' })`<br>`@JoinColumn({ name: 'folder_id' })` |
| `listing` | Yes | `Listing` | `@ManyToOne(() => Listing, { onDelete: 'NO ACTION' })`<br>`@JoinColumn({ name: 'listing_id', referencedColumnName: 'listingId' })` |

## class FolderListingEdge

- Source: `src/folder/dto/paginated-folder-listings.dto.ts:4`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `listing` | Yes | `ListingDTO` |  |
| `rank` | Yes | `string` |  |
| `addedAt` | Yes | `Date` |  |

## type FolderListingRankRow

- Source: `src/migrations/1777500000001-AddUniqueFolderListingRank.ts:4`
- Type: `{ folder_id: string; listing_id: string; }`

## interface FolderRollups
_S3 key of the first listing's thumbnail asset (null when no qualifying listing exists)._

- Source: `src/folder/services/folder-rollup.types.ts:1`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `listingCount` | Yes | `bigint` |  |
| `totalLikes` | Yes | `bigint` |  |
| `totalViews` | Yes | `bigint` |  |
| `priceMin` | Yes | `number \| null` |  |
| `priceMax` | Yes | `number \| null` |  |
| `childLastUpdatedAt` | Yes | `Date \| null` |  |
| `mediaTypes` | Yes | `string[] \| undefined` |  |
| `firstListingThumbnailKey` | Yes | `string \| null` |  |

## class FolderSearchCard

- Source: `src/search/dto/folder-search-card.dto.ts:4`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `id` | Yes | `string` |  |
| `name` | Yes | `string` |  |
| `description` | No | `string` |  |
| `tags` | No | `string[]` |  |
| `type` | Yes | `FolderType` |  |
| `ownerId` | Yes | `string` |  |
| `ownerUserName` | Yes | `string` |  |
| `ownerName` | No | `string` |  |
| `thumbnailUrl` | No | `string` |  |
| `effectiveThumbnailUrl` | No | `string` |  |
| `url` | Yes | `string` |  |
| `likeCount` | Yes | `number` |  |
| `saveCount` | Yes | `number` |  |
| `followCount` | Yes | `number` |  |
| `viralScore` | Yes | `number` |  |
| `listingCount` | Yes | `number` |  |
| `totalLikes` | Yes | `number` |  |
| `totalViews` | Yes | `number` |  |
| `mediaTypes` | No | `string[]` |  |
| `priceMin` | No | `number` |  |
| `priceMax` | No | `number` |  |

## enum FolderSortBy

- Source: `src/search/dto/search-folders.input.ts:5`

| Member | Value |
|---|---|
| `viralScore` | `'viralScore'` |
| `listingCount` | `'listingCount'` |
| `createdAt` | `'createdAt'` |
| `childLastUpdatedAt` | `'childLastUpdatedAt'` |

## enum FolderType

- Source: `src/folder/entities/folder.entity.ts:21`

| Member | Value |
|---|---|
| `PROFILE` | `'PROFILE'` |
| `PORTFOLIO` | `'PORTFOLIO'` |
| `COLLECTION` | `'COLLECTION'` |
| `PLAYLIST` | `'PLAYLIST'` |

## type FolderViralKind

- Source: `src/viral-score/folder-viral-score.service.ts:33`
- Type: `keyof typeof FOLDER_VIRAL_WEIGHTS`

## enum FolderVisibility

- Source: `src/folder/entities/folder.entity.ts:28`

| Member | Value |
|---|---|
| `PUBLIC` | `'PUBLIC'` |
| `PRIVATE` | `'PRIVATE'` |

## type FolderWithQueueCaches

- Source: `src/agent/controllers/agent-feed-queue.controller.ts:23`
- Type: `Folder & { __firstListingThumbnailUrl?: string \| null; __ownerListingCount?: number; }`

## type FolderWithThumbnailCache

- Source: `src/agent/services/agent-activity-formatter.service.ts:46`
- Type: `Folder & { __firstListingThumbnailUrl?: string \| null; }`

## class Follow

- Source: `src/activity/entities/follow.entity.ts:16`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `followId` | Yes | `string` | `@PrimaryGeneratedColumn('uuid', { name: 'follow_id' })` |
| `followerId` | Yes | `string` | `@Column({ name: 'follower_id' })` |
| `follower` | Yes | `User` | `@ManyToOne(() => User, (follower) => follower.from)`<br>`@JoinColumn([{ name: 'follower_id', referencedColumnName: 'userId' }])` |
| `followingId` | Yes | `string` | `@Column({ name: 'following_id' })` |
| `following` | Yes | `User` | `@ManyToOne(() => User, (following) => following.followings)`<br>`@JoinColumn([{ name: 'following_id', referencedColumnName: 'userId' }])` |
| `createdAt` | Yes | `Date` | `@CreateDateColumn({ name: 'created_at' })` |
| `updatedAt` | Yes | `Date` | `@UpdateDateColumn({ name: 'updated_at' })` |
| `deletedAt` | Yes | `Date` | `@DeleteDateColumn({ name: 'deleted_at' })` |

## enum FraudStatus

- Source: `src/fraud/fraud-detection.service.ts:19`

| Member | Value |
|---|---|
| `CLEAN` | `'clean'` |
| `WITHHELD` | `'withheld'` |
| `FLAGGED` | `'flagged'` |

## class GetAdminAssetsDTO

- Source: `src/listing/dto/getAdminAssets.dto.ts:10`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `from` | Yes | `number` | `@IsNumber` |
| `count` | Yes | `number` | `@IsNumber`<br>`@Max(100)` |
| `nameFilter` | Yes | `string` | `@IsString`<br>`@IsOptional` |
| `searchKey` | Yes | `string` | `@IsString`<br>`@IsOptional` |
| `violationFilter` | Yes | `string` | `@IsString`<br>`@IsOptional` |
| `fileTypeFilter` | Yes | `string` | `@IsString`<br>`@IsOptional` |
| `dateRange` | No | `[Date, Date]` | `@IsOptional` |
| `showReviewed` | No | `boolean` | `@IsBoolean`<br>`@IsOptional` |

## class GetAdminCommentsDTO

- Source: `src/activity/dto/getAdminComments.dto.ts:10`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `from` | Yes | `number` | `@IsNumber` |
| `count` | Yes | `number` | `@IsNumber`<br>`@Max(100)` |
| `searchKey` | Yes | `string` | `@IsString`<br>`@IsOptional` |
| `nameFilter` | Yes | `string` | `@IsString`<br>`@IsOptional` |
| `listingFilter` | Yes | `string` | `@IsString`<br>`@IsOptional` |
| `commentFilter` | Yes | `string` | `@IsString`<br>`@IsOptional` |
| `parentCommentFilter` | Yes | `string` | `@IsString`<br>`@IsOptional` |
| `dateRange` | No | `[Date, Date]` | `@IsOptional` |
| `showFlagged` | No | `boolean` | `@IsBoolean`<br>`@IsOptional` |
| `showHidden` | No | `boolean` | `@IsBoolean`<br>`@IsOptional` |

## class GetAllPointEarnedDTO

- Source: `src/point/dto/getAllPointEarned.dto.ts:4`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `from` | Yes | `number` | `@IsNumber` |
| `count` | Yes | `number` | `@IsNumber`<br>`@Max(100)` |
| `searchKey` | Yes | `string` | `@IsString`<br>`@IsOptional` |
| `nameFilter` | Yes | `string` | `@IsString`<br>`@IsOptional` |
| `typeFilter` | Yes | `string` | `@IsString`<br>`@IsOptional` |
| `amountRangeFrom` | No | `number` | `@IsOptional` |
| `amountRangeTo` | No | `number` | `@IsOptional` |
| `dateRange` | No | `[Date, Date]` | `@IsOptional` |

## class GetAllUsersDTO

- Source: `src/user/dto/getAllUsersInput.dto.ts:4`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `from` | Yes | `number` | `@IsNumber` |
| `count` | Yes | `number` | `@IsNumber`<br>`@Max(100)` |

## class GetAllUsersReponseWithTotalDTO

- Source: `src/user/dto/getAllUsersResponse.dto.ts:4`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `users` | Yes | `AdminUser[]` |  |
| `total` | Yes | `number` |  |

## class GetListingCommentsDTO

- Source: `src/activity/dto/getListingComments.dto.ts:4`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `from` | Yes | `number` | `@IsNumber` |
| `count` | Yes | `number` | `@IsNumber`<br>`@Max(100)` |
| `listingId` | Yes | `string` | `@IsUUID` |
| `parentId` | No | `string` | `@IsUUID`<br>`@IsOptional` |

## class GetPayTokensDTO

- Source: `src/listing/dto/getPayTokens.dto.ts:5`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `from` | Yes | `number` | `@IsNumber` |
| `count` | Yes | `number` | `@IsNumber`<br>`@Max(100)` |
| `status` | Yes | `TokenStatus` | `@IsEnum(TokenStatus)`<br>`@IsOptional` |
| `userNameFilter` | Yes | `string` | `@IsString`<br>`@IsOptional` |
| `nameFilter` | Yes | `string` | `@IsString`<br>`@IsOptional` |
| `symbolFilter` | Yes | `string` | `@IsString`<br>`@IsOptional` |
| `addressFilter` | Yes | `string` | `@IsString`<br>`@IsOptional` |
| `communityNameFilter` | Yes | `string` | `@IsString`<br>`@IsOptional` |
| `searchKey` | Yes | `string` | `@IsString`<br>`@IsOptional` |
| `dateRange` | No | `[Date, Date]` | `@IsOptional` |

## class GetUserInteractionsDTO

- Source: `src/search/dto/listing-interaction.dto.ts:25`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `listingIds` | Yes | `string[]` | `@IsArray`<br>`@IsUUID('all', { each: true })`<br>`@ArrayMaxSize(50)` |

## enum GraphQLErrorCode

- Source: `src/utils/graphql-error-codes.ts:4`

| Member | Value |
|---|---|
| `UNAUTHENTICATED` | `'UNAUTHENTICATED'` |
| `FORBIDDEN` | `'FORBIDDEN'` |
| `NOT_FOUND` | `'NOT_FOUND'` |
| `RATE_LIMITED` | `'RATE_LIMITED'` |
| `VALIDATION_ERROR` | `'VALIDATION_ERROR'` |
| `INTERNAL_ERROR` | `'INTERNAL_ERROR'` |
| `CONFLICT` | `'CONFLICT'` |

## type HydratableFeedRow

- Source: `src/user-feed-queue/services/feed-target-hydration.service.ts:21`
- Type: `{ targetType: FeedTargetType; targetId: string; __hydratedTarget?: FeedTargetUnion \| null; }`

## class IdempotencyKey

- Source: `src/billing/entities/idempotency-key.entity.ts:9`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `id` | Yes | `string` | `@PrimaryGeneratedColumn('uuid', { name: 'id' })` |
| `userId` | Yes | `string` | `@Column({ name: 'user_id', type: 'uuid' })` |
| `requestKey` | Yes | `string` | `@Column({ name: 'request_key' })` |
| `responseData` | Yes | `Record<string, any>` | `@Column({ name: 'response_data', type: 'jsonb', nullable: true })` |
| `expiresAt` | Yes | `Date` | `@Column({ name: 'expires_at', type: 'timestamptz' })` |
| `createdAt` | Yes | `Date` | `@CreateDateColumn({ name: 'created_at' })` |

## interface IdempotentHttpOptions

- Source: `src/resilience/idempotency/idempotent-http.factory.ts:12`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `provider` | Yes | `Provider` |  |
| `timeout` | No | `number` |  |

## interface InAppPayload

- Source: `src/notifications/types/payloads.ts:23`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `title` | Yes | `string` |  |
| `message` | Yes | `string` |  |
| `link` | No | `string` |  |

## class InputArrayNumber

- Source: `src/utils/generalGraphqlModel.dto.ts:39`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `ids` | Yes | `[number]` |  |

## class InputArrayUUID

- Source: `src/utils/generalGraphqlModel.dto.ts:45`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `ids` | Yes | `[string]` |  |

## class InputETH

- Source: `src/utils/generalGraphqlModel.dto.ts:11`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `address` | Yes | `string` | `@IsEthereumAddress` |

## class InputName

- Source: `src/utils/generalGraphqlModel.dto.ts:25`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `name` | Yes | `string` | `@IsString` |

## class InputNumber

- Source: `src/utils/generalGraphqlModel.dto.ts:32`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `id` | Yes | `number` | `@IsNumber` |

## class InputPayPalEstimateDTO
_@deprecated No longer used server-side — kept for backward compatibility with frontend callers._

- Source: `src/paypal/dto/inputPayPalEstimate.dto.ts:4`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `listingId` | No | `string` | `@IsUUID`<br>`@IsOptional` |
| `price` | Yes | `number` | `@IsNumber({ maxDecimalPlaces: 2 })`<br>`@Min(0)` |

## class InputString

- Source: `src/utils/generalGraphqlModel.dto.ts:18`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `id` | Yes | `string` | `@IsString` |

## class InputUUID

- Source: `src/utils/generalGraphqlModel.dto.ts:4`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `id` | Yes | `string` | `@IsUUID` |

## class InteractionsTotalDTO

- Source: `src/activity/dto/interactionsTotal.dto.ts:3`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `likes` | Yes | `number` |  |
| `favorites` | Yes | `number` |  |

## class ItemCanceledDTO

- Source: `src/marketplace/dto/itemCanceled.dto.ts:4`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `transactionHash` | Yes | `string` | `@IsString` |
| `blockNumber` | Yes | `number` | `@IsNumber` |
| `ownerC` | Yes | `string` | `@IsString` |
| `tokenId` | Yes | `number` | `@IsNumber` |

## class ItemListedDTO

- Source: `src/marketplace/dto/itemListed.dto.ts:4`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `transactionHash` | Yes | `string` | `@IsString` |
| `blockNumber` | Yes | `number` | `@IsNumber` |
| `ownerC` | Yes | `string` | `@IsEthereumAddress` |
| `tokenId` | Yes | `number` | `@IsNumber` |
| `pricePerItem` | Yes | `string` | `@IsString` |

## class ItemsByDateDTO

- Source: `src/utils/generalGraphqlModel.dto.ts:57`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `date` | Yes | `string` |  |
| `count` | Yes | `number` |  |

## class ItemSoldDTO

- Source: `src/marketplace/dto/itemSold.dto.ts:4`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `transactionHash` | Yes | `string` | `@IsString` |
| `sellerC` | Yes | `string` | `@IsString` |
| `buyerC` | Yes | `string` | `@IsString` |
| `tokenId` | Yes | `number` | `@IsNumber` |
| `pricePerItem` | Yes | `string` |  |

## class ItemUpdatedDTO

- Source: `src/marketplace/dto/itemUpdated.dto.ts:4`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `transactionHash` | Yes | `string` | `@IsString` |
| `blockNumber` | Yes | `number` | `@IsNumber` |
| `ownerC` | Yes | `string` | `@IsString` |
| `tokenId` | Yes | `number` | `@IsNumber` |
| `newPricePerItem` | Yes | `string` | `@IsString` |

## class LeaderboardDTO

- Source: `src/analytics/dto/leaderboard.dto.ts:24`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `entries` | Yes | `LeaderboardEntryDTO[]` |  |
| `period` | Yes | `string` |  |
| `sortBy` | Yes | `string` |  |

## class LeaderboardEntryDTO

- Source: `src/analytics/dto/leaderboard.dto.ts:3`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `userId` | Yes | `string` |  |
| `userName` | No | `string` |  |
| `rank` | Yes | `number` |  |
| `sales` | Yes | `number` |  |
| `revenue` | Yes | `number` |  |
| `followerCount` | No | `number` |  |

## class LicenseSaleItemDTO

- Source: `src/activity/dto/license-sales.dto.ts:3`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `amount` | Yes | `string` |  |
| `amountInUSD` | Yes | `string` |  |
| `createdAt` | Yes | `Date` |  |

## class LicenseSalesAggregateDTO

- Source: `src/activity/dto/license-sales.dto.ts:15`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `totalLicenseSales` | Yes | `number` |  |
| `totalLicenseRevenue` | Yes | `number` |  |
| `averageLicensePrice` | Yes | `number` |  |
| `lastSaleDate` | No | `Date` |  |
| `firstSaleDate` | No | `Date` |  |

## class LicenseSalesDTO

- Source: `src/activity/dto/license-sales.dto.ts:33`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `items` | Yes | `LicenseSaleItemDTO[]` |  |
| `aggregates` | Yes | `LicenseSalesAggregateDTO` |  |

## class Like

- Source: `src/activity/entities/like.entity.ts:15`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `likeId` | Yes | `string` | `@PrimaryGeneratedColumn('uuid', { name: 'like_id' })` |
| `listingId` | Yes | `string` | `@Column({ name: 'listing_id' })` |
| `listing` | Yes | `Listing` | `@ManyToOne(() => Listing, (listing) => listing.likes)`<br>`@JoinColumn({ name: 'listing_id', referencedColumnName: 'listingId' })` |
| `userId` | Yes | `string` | `@Column({ name: 'user_id' })` |
| `user` | Yes | `User` | `@ManyToOne(() => User, (user) => user.likes)`<br>`@JoinColumn({ name: 'user_id', referencedColumnName: 'userId' })` |
| `createdAt` | Yes | `Date` | `@CreateDateColumn({ name: 'created_at' })` |

## class LimitQueryDto

- Source: `src/agent/dto/analytics-query.dto.ts:29`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `limit` | No | `number` | `@IsOptional`<br>`@Type(() => Number)`<br>`@IsInt`<br>`@Min(1)`<br>`@Max(50)` |

## class LinkCompleteDto

- Source: `src/agent/dto/link-complete.dto.ts:3`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `token` | Yes | `string` | `@IsNotEmpty`<br>`@IsString` |

## interface LinkPreviewResponse

- Source: `src/agent/dto/link-complete.dto.ts:29`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `agent_id` | Yes | `string` |  |
| `agent_name` | Yes | `string` |  |
| `agent_email` | Yes | `string` |  |

## interface LinkStatusResponse

- Source: `src/agent/dto/link-complete.dto.ts:15`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `linked` | Yes | `boolean` |  |
| `operator` | Yes | `{ id: string; name: string \| null; email: string; linked_at: string \| null; } \| null` |  |
| `pending` | Yes | `{ operator_email: string; created_at: string; } \| null` |  |

## class Listing

- Source: `src/listing/entities/listing.entity.ts:39`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `listingId` | Yes | `string` | `@PrimaryGeneratedColumn('uuid', { name: 'listing_id' })` |
| `userId` | Yes | `string` | `@Column({ name: 'user_id' })` |
| `user` | Yes | `User` | `@ManyToOne(() => User, (user) => user.listings)`<br>`@JoinColumn({ name: 'user_id', referencedColumnName: 'userId' })` |
| `artistId` | Yes | `string` | `@Column({ name: 'artist_id', nullable: true })` |
| `artist` | Yes | `User` | `@ManyToOne(() => User, (user) => user.createdListings)`<br>`@JoinColumn({ name: 'artist_id', referencedColumnName: 'userId' })` |
| `name` | Yes | `string` | `@Column('character varying', { name: 'name' })` |
| `slug` | Yes | `string` | `@Column('character varying', { name: 'slug', nullable: true })` |
| `description` | Yes | `string` | `@Column('character varying', { name: 'description' })` |
| `processing` | Yes | `ListingProcessResult` | `@Column({ type: 'enum', enum: ListingProcessResult, name: 'processing', default: null, })` |
| `royalty` | Yes | `number` | `@Column('integer', { name: 'royalty' })` |
| `categoryId` | Yes | `number` | `@Column({ name: 'category_id' })` |
| `category` | Yes | `Category` | `@ManyToOne(() => Category, (category) => category.listings)`<br>`@JoinColumn([{ name: 'category_id', referencedColumnName: 'categoryId' }])` |
| `contractTypeId` | Yes | `number` | `@Column({ name: 'contract_type_id' })` |
| `contractType` | Yes | `ContractType` | `@ManyToOne(() => ContractType, (contractType) => contractType.listings)`<br>`@JoinColumn({ name: 'contract_type_id', referencedColumnName: 'contractTypeId', })` |
| `listingStatusId` | Yes | `number` | `@Column('integer', { name: 'listing_status_id', nullable: true })` |
| `listingStatus` | Yes | `ListingStatus` | `@ManyToOne(() => ListingStatus, (status) => status.listings)`<br>`@JoinColumn([ { name: 'listing_status_id', referencedColumnName: 'listingStatusId' }, ])` |
| `rejectReason` | Yes | `string` | `@Column('character varying', { name: 'reject_reason', nullable: true })` |
| `listingToAssets` | Yes | `ListingToAsset[]` | `@OneToMany(() => ListingToAsset, (listingToAssets) => listingToAssets.listing)` |
| `listingToTags` | Yes | `ListingToTag[]` | `@OneToMany(() => ListingToTag, (listingToTag) => listingToTag.listing)` |
| `listingToSubcategories` | Yes | `ListingToSubcategory[]` | `@OneToMany(() => ListingToSubcategory, (listingToSubcategory) => listingToSubcategory.listing)` |
| `contractAddress` | Yes | `string` | `@Column('character varying', { name: 'contract_address', nullable: true })` |
| `paymentMethod` | Yes | `ListingPaymentMethod` | `@Column({ type: 'enum', enum: ListingPaymentMethod, name: 'payment_method', nullable: true, })` |
| `attributes` | Yes | `string` | `@Column('character varying', { name: 'atributes', nullable: true })` |
| `prompt` | Yes | `string` | `@Column('text', { name: 'prompt', nullable: true })` |
| `model` | Yes | `string` | `@Column('text', { name: 'model', nullable: true })` |
| `price` | Yes | `number` | `@Column('float', { name: 'price', nullable: true })` |
| `downloadPrice` | Yes | `number` | `@Column('float', { name: 'download_price', nullable: true })` |
| `lastSalePrice` | Yes | `number` | `@Column({ name: 'last_sale_price', type: 'numeric', precision: 12, scale: 2, nullable: true, })` |
| `listedAt` | Yes | `Date` | `@Column('timestamptz', { name: 'listed_at', nullable: true })` |
| `soldAt` | Yes | `Date` | `@Column('timestamptz', { name: 'sold_at', nullable: true })` |
| `saleEndsAt` | Yes | `Date` | `@Column('timestamptz', { name: 'sale_ends_at', nullable: true })` |
| `payTokenId` | Yes | `number` | `@Column('integer', { name: 'pay_token_id', nullable: true })` |
| `payToken` | Yes | `PayToken` | `@ManyToOne(() => PayToken, (payToken) => payToken.listings)`<br>`@JoinColumn([{ name: 'pay_token_id', referencedColumnName: 'payTokenId' }])` |
| `listingContractId` | Yes | `number` | `@Column('integer', { name: 'listing_contract_id', nullable: true })` |
| `mintTxHash` | Yes | `string` | `@Column('character varying', { name: 'mint_tx_hash', nullable: true })` |
| `metadataUri` | Yes | `string` | `@Column('character varying', { name: 'metadata_uri', nullable: true })` |
| `sellingStatusId` | Yes | `number` | `@Column({ name: 'selling_status_id', nullable: true })` |
| `sellingStatus` | Yes | `SellingStatus` | `@ManyToOne(() => SellingStatus, (sellingStatus) => sellingStatus.listings)`<br>`@JoinColumn({ name: 'selling_status_id', referencedColumnName: 'sellingStatusId', })` |
| `likes` | Yes | `Like[]` | `@OneToMany(() => Like, (likes) => likes.listing)` |
| `views` | Yes | `View[]` | `@OneToMany(() => View, (views) => views.listing)` |
| `downloads` | Yes | `Download[]` | `@OneToMany(() => Download, (downloads) => downloads.listing)` |
| `transactions` | Yes | `Transaction[]` | `@OneToMany(() => Transaction, (transaction) => transaction.listing)` |
| `tradeHistories` | Yes | `TradeHistory[]` | `@OneToMany(() => TradeHistory, (tradeHistories) => tradeHistories.listing)` |
| `eventLedgerEntries` | Yes | `EventLedger[]` | `@OneToMany(() => EventLedger, (el) => el.listing)` |
| `bids` | Yes | `Bid[]` | `@OneToMany(() => Bid, (bids) => bids.listing)` |
| `offers` | Yes | `Offer[]` | `@OneToMany(() => Offer, (offers) => offers.listing)` |
| `comments` | Yes | `Comment[]` | `@OneToMany(() => Comment, (comment) => comment.listing)` |
| `flags` | Yes | `ListingFlag[]` | `@OneToMany(() => ListingFlag, (listingFlag) => listingFlag.listing, { cascade: true, })` |
| `processLogs` | Yes | `ListingProcessLog[]` | `@OneToMany(() => ListingProcessLog, (listingProcessLog) => listingProcessLog.listing, { cascade: true, })` |
| `createdAt` | Yes | `Date` | `@CreateDateColumn({ name: 'created_at' })` |
| `updatedAt` | Yes | `Date` | `@UpdateDateColumn({ name: 'updated_at' })` |
| `deletedAt` | Yes | `Date` | `@DeleteDateColumn({ name: 'deleted_at' })` |
| `viralScore` | Yes | `number` | `@Column('float', { name: 'viral_score', nullable: true, default: 0 })` |
| `viralScoreUpdatedAt` | Yes | `Date` | `@Column('timestamptz', { name: 'viral_score_updated_at', nullable: true })` |
| `fraudScore` | Yes | `number` | `@Column({ name: 'fraud_score', type: 'float', default: 0 })` |
| `fraudStatus` | Yes | `string` | `@Column({ name: 'fraud_status', type: 'varchar', default: 'clean' })` |
| `likeCount` | Yes | `number` | `@Column({ name: 'like_count', type: 'int', default: 0 })` |
| `saveCount` | Yes | `number` | `@Column({ name: 'save_count', type: 'int', default: 0 })` |
| `viewCount` | Yes | `number` | `@Column({ name: 'view_count', type: 'int', default: 0 })` |
| `purchaseCount` | Yes | `number` | `@Column({ name: 'purchase_count', type: 'int', default: 0 })` |
| `commentCount` | Yes | `number` | `@Column({ name: 'comment_count', type: 'int', default: 0 })` |
| `shareCount` | Yes | `number` | `@Column({ name: 'share_count', type: 'int', default: 0 })` |
| `isPrivate` | Yes | `boolean` | `@Column({ name: 'is_private', type: 'boolean', default: false })` |
| `freeDownload` | Yes | `boolean` | `@Column({ name: 'free_download', type: 'boolean', default: false })` |
| `processingAttempts` | Yes | `number` | `@Column({ name: 'processing_attempts', type: 'int', default: 0 })` |
| `processingFailureReason` | Yes | `string \| null` | `@Column({ name: 'processing_failure_reason', type: 'varchar', length: 64, nullable: true, })` |
| `salesCount` | Yes | `number` | `@Column({ name: 'sales_count', type: 'int', default: 0 })` |
| `totalRevenue` | Yes | `number` | `@Column({ name: 'total_revenue', type: 'numeric', precision: 12, scale: 2, default: 0, })` |
| `floorPrice` | Yes | `number` | `@Column({ name: 'floor_price', type: 'numeric', precision: 12, scale: 2, nullable: true, })` |
| `ownershipSalesCount` | Yes | `number` | `@Column({ name: 'ownership_sales_count', type: 'int', default: 0 })` |
| `downloadSalesCount` | Yes | `number` | `@Column({ name: 'download_sales_count', type: 'int', default: 0 })` |
| `ownershipRevenue` | Yes | `number` | `@Column({ name: 'ownership_revenue', type: 'numeric', precision: 12, scale: 2, default: 0, })` |
| `downloadRevenue` | Yes | `number` | `@Column({ name: 'download_revenue', type: 'numeric', precision: 12, scale: 2, default: 0, })` |
| `manifestSummary` | Yes | `ZipManifestSummary \| null` | `@Column('jsonb', { name: 'manifest_summary', nullable: true })` |
| `manifestUrl` | Yes | `string \| null` | `@Column('text', { name: 'manifest_url', nullable: true })` |

## class ListingActivityDTO

- Source: `src/activity/dto/listing-activity.dto.ts:6`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `tradeHistories` | Yes | `TradeHistoryDTO[]` |  |
| `offers` | Yes | `OfferDTO[]` |  |
| `licenseSales` | Yes | `LicenseSalesDTO` |  |

## class ListingAnalyticsDTO

- Source: `src/analytics/dto/listing-analytics.dto.ts:3`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `listingId` | Yes | `string` |  |
| `viewCount` | Yes | `number` |  |
| `likeCount` | Yes | `number` |  |
| `saveCount` | Yes | `number` |  |
| `commentCount` | Yes | `number` |  |
| `purchaseCount` | Yes | `number` |  |
| `salesCount` | Yes | `number` |  |
| `ownershipSalesCount` | Yes | `number` |  |
| `downloadSalesCount` | Yes | `number` |  |
| `ownershipRevenue` | Yes | `number` |  |
| `downloadRevenue` | Yes | `number` |  |
| `totalRevenue` | Yes | `number` |  |
| `lastSalePrice` | No | `number` |  |
| `floorPrice` | No | `number` |  |
| `conversionRate` | No | `number` |  |

## type ListingAssetLike

- Source: `src/agent/services/agent-activity-formatter.service.ts:45`
- Type: `AssetPresentationShape`

## type ListingAssetRow

- Source: `src/user-feed-queue/services/feed-target-hydration.service.ts:34`
- Type: `AssetPresentationShape & { listingId: string; }`

## interface ListingContext
_Minimal listing fields needed for engagement notifications._

- Source: `src/engagement/engagement.service.ts:21`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `userId` | Yes | `string` |  |
| `artistId` | No | `string \| null` |  |
| `name` | Yes | `string` |  |
| `slug` | Yes | `string` |  |

## type ListingContractTypes

- Source: `src/utils/types.ts:6`
- Type: `\| 'Exclusive Contract' \| 'Non-Exclusive Contract' \| 'Public Domain'`

## enum ListingCounter

- Source: `src/counter/counter.types.ts:6`

| Member | Value |
|---|---|
| `LIKE` | `'likeCount'` |
| `VIEW` | `'viewCount'` |
| `SHARE` | `'shareCount'` |
| `COMMENT` | `'commentCount'` |
| `SAVE` | `'saveCount'` |

## class ListingDTO

- Source: `src/listing/dto/listing.dto.ts:18`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `convertAttributes` | Yes | `inferred` |  |
| `listingId` | Yes | `string` |  |
| `userId` | Yes | `string` |  |
| `user` | Yes | `PublicUser` |  |
| `artistId` | Yes | `string` |  |
| `artist` | Yes | `PublicUser` |  |
| `listingContractId` | Yes | `number` |  |
| `mintTxHash` | Yes | `string` |  |
| `name` | Yes | `string` |  |
| `slug` | Yes | `string` |  |
| `description` | Yes | `string` |  |
| `prompt` | No | `string` |  |
| `model` | No | `string` |  |
| `listingStatusId` | Yes | `number` |  |
| `listingStatus` | Yes | `ListingStatus` |  |
| `attributes` | Yes | `AttributeType[]` |  |
| `listingAssets` | Yes | `Asset[]` |  |
| `tags` | Yes | `Tag[]` |  |
| `contractAddress` | Yes | `string` |  |
| `price` | Yes | `number` |  |
| `downloadPrice` | Yes | `number` |  |
| `lastSalePrice` | Yes | `number` |  |
| `listedAt` | Yes | `Date` |  |
| `soldAt` | Yes | `Date` |  |
| `saleEndsAt` | Yes | `Date` |  |
| `payTokenId` | Yes | `number` |  |
| `payToken` | Yes | `PayToken` |  |
| `royalty` | Yes | `number` |  |
| `categoryId` | Yes | `number` |  |
| `category` | Yes | `Category` |  |
| `subcategories` | Yes | `Category[]` |  |
| `subsubcategories` | Yes | `Category[]` |  |
| `metadataUri` | Yes | `string` |  |
| `paymentMethod` | Yes | `ListingPaymentMethod` |  |
| `contractTypeId` | Yes | `number` |  |
| `contractType` | Yes | `ContractType` |  |
| `sellingStatusId` | Yes | `number` |  |
| `sellingStatus` | Yes | `SellingStatus` |  |
| `likes` | Yes | `number` |  |
| `favorites` | Yes | `number` |  |
| `views` | Yes | `number` |  |
| `shares` | Yes | `number` |  |
| `comments` | Yes | `number` |  |
| `viralScore` | Yes | `number` |  |
| `rank` | Yes | `number` |  |
| `isLiked` | Yes | `boolean` |  |
| `isFavorite` | Yes | `boolean` |  |
| `isViewed` | Yes | `boolean` |  |
| `hasOffer` | Yes | `boolean` |  |
| `hasBids` | Yes | `boolean` |  |
| `onAuction` | Yes | `boolean` |  |
| `onListing` | Yes | `boolean` |  |
| `isFlagged` | No | `boolean` |  |
| `isHidden` | No | `boolean` |  |
| `isPrivate` | No | `boolean` |  |
| `freeDownload` | No | `boolean` |  |
| `processing` | No | `ListingProcessResult` |  |
| `zipManifestSummary` | No | `ZipManifestSummaryType` |  |
| `sourceMetadata` | No | `SourceMetadataType` |  |
| `createdAt` | Yes | `Date` |  |

## class ListingEngagementStateResponse

- Source: `src/agent/dto/social-engagement.dto.ts:72`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `liked` | Yes | `boolean` |  |
| `saved` | Yes | `boolean` |  |

## class ListingEventDTO

- Source: `src/listing/dto/listingEvent.dto.ts:4`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `tokenUri` | Yes | `string` | `@IsString` |
| `tokenId` | Yes | `number` | `@IsNumber` |
| `txHash` | No | `string` | `@IsString`<br>`@IsOptional` |

## class ListingFileResponseDTO

- Source: `src/listing/dto/listingFileResponse.dto.ts:3`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `signedURL` | Yes | `string` |  |
| `fileName` | Yes | `string` |  |
| `contentLength` | Yes | `number` |  |

## class ListingFlag

- Source: `src/listing/entities/listingFlag.entity.ts:18`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `listingFlagId` | Yes | `string` | `@PrimaryGeneratedColumn('uuid', { name: 'listing_flag_id' })` |
| `violation` | Yes | `string` | `@Column({ length: 250 })` |
| `status` | No | `FlagType` | `@Column({ type: 'enum', enum: FlagType })` |
| `userId` | Yes | `string` | `@Column({ name: 'user_id' })` |
| `user` | Yes | `User` | `@ManyToOne(() => User, (user) => user.listingFlags)`<br>`@JoinColumn({ name: 'user_id', referencedColumnName: 'userId' })` |
| `listingId` | Yes | `string` | `@Column({ name: 'listing_id' })` |
| `listing` | Yes | `Listing` | `@ManyToOne(() => Listing, (listing) => listing.flags)`<br>`@JoinColumn({ name: 'listing_id', referencedColumnName: 'listingId' })` |
| `createdAt` | Yes | `Date` | `@CreateDateColumn({ name: 'created_at' })` |
| `updatedAt` | Yes | `Date` | `@UpdateDateColumn({ name: 'updated_at' })` |
| `deletedAt` | Yes | `Date` | `@DeleteDateColumn({ name: 'deleted_at' })` |

## class ListingFlagDTO

- Source: `src/listing/dto/listingFlag.dto.ts:5`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `listingFlagId` | Yes | `string` |  |
| `violation` | Yes | `string` |  |
| `userId` | Yes | `string` |  |
| `user` | Yes | `PublicUser` |  |

## class ListingInteractionDTO

- Source: `src/search/dto/listing-interaction.dto.ts:4`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `listingId` | Yes | `string` |  |
| `isLiked` | Yes | `boolean` |  |
| `isFavorite` | Yes | `boolean` |  |
| `isFollowing` | Yes | `boolean` |  |
| `hasLicense` | Yes | `boolean` |  |
| `hasMyOffer` | Yes | `boolean` |  |

## class ListingLikeMutationResponse

- Source: `src/agent/dto/social-engagement.dto.ts:60`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `liked` | Yes | `boolean` |  |
| `changed` | Yes | `boolean` |  |
| `action` | Yes | `'liked' \| 'already_liked' \| 'unliked' \| 'already_unliked'` |  |

## class ListingMetadataDTO

- Source: `src/listing/dto/listingMetadata.dto.ts:3`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `contentLength` | Yes | `number` |  |
| `contentType` | Yes | `string` |  |
| `name` | Yes | `string` |  |

## class ListingMetricsResponse

- Source: `src/agent/dto/social-engagement.dto.ts:85`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `likes` | Yes | `number` |  |
| `views` | Yes | `number` |  |
| `shares` | Yes | `number` |  |
| `comments` | Yes | `number` |  |
| `viral_score` | Yes | `number` |  |

## class ListingOffersQueryDto

- Source: `src/agent/dto/offer.dto.ts:55`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `listing_id` | Yes | `string` | `@IsUUID` |

## enum ListingPaymentMethod

- Source: `src/utils/types.ts:85`

| Member | Value |
|---|---|
| `CRYPTO` | `'crypto'` |
| `FIAT` | `'fiat'` |

## class ListingProcessLog

- Source: `src/listing/entities/listingProcessLog.entity.ts:15`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `listingProcessLogId` | Yes | `string` | `@PrimaryGeneratedColumn('uuid', { name: 'listing_process_log_id' })` |
| `error` | Yes | `string` | `@Column` |
| `type` | No | `ListingProcessLogType` | `@Column({ type: 'enum', enum: ListingProcessLogType })` |
| `listingId` | Yes | `string` | `@Column({ name: 'listing_id' })` |
| `listing` | Yes | `Listing` | `@ManyToOne(() => Listing, (listing) => listing.processLogs)`<br>`@JoinColumn({ name: 'listing_id', referencedColumnName: 'listingId' })` |
| `createdAt` | Yes | `Date` | `@CreateDateColumn({ name: 'created_at' })` |
| `deletedAt` | Yes | `Date` | `@DeleteDateColumn({ name: 'deleted_at' })` |

## enum ListingProcessLogType

- Source: `src/utils/types.ts:75`

| Member | Value |
|---|---|
| `AUDIO` | `'audio'` |
| `VIDEO` | `'video'` |

## enum ListingProcessResult

- Source: `src/listing/utils/listingStatus.ts:41`

| Member | Value |
|---|---|
| `PENDING` | `'pending'` |
| `FAILED` | `'failed'` |

## class ListingResponseWithTotalDTO

- Source: `src/listing/dto/listingResponseWithTotal.dto.ts:4`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `listings` | Yes | `ListingDTO[]` |  |
| `total` | Yes | `number` |  |

## class ListingSaveMutationResponse

- Source: `src/agent/dto/social-engagement.dto.ts:66`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `saved` | Yes | `boolean` |  |
| `changed` | Yes | `boolean` |  |
| `action` | Yes | `'saved' \| 'already_saved' \| 'unsaved' \| 'already_unsaved'` |  |

## class ListingStatus

- Source: `src/listing/entities/listingStatus.entity.ts:13`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `listingStatusId` | Yes | `number` | `@PrimaryGeneratedColumn({ name: 'listing_status_id' })` |
| `name` | Yes | `string` | `@Column('character varying', { name: 'name' })` |
| `listings` | Yes | `Listing[]` | `@OneToMany(() => Listing, (listings) => listings.listingStatus)` |
| `createdAt` | Yes | `Date` | `@CreateDateColumn({ name: 'created_at' })` |
| `updatedAt` | Yes | `Date` | `@UpdateDateColumn({ name: 'updated_at' })` |
| `deletedAt` | Yes | `Date` | `@DeleteDateColumn({ name: 'deleted_at' })` |

## class ListingStatusResponseDTO

- Source: `src/listing/dto/listingStatusResponse.dto.ts:5`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `status` | Yes | `ListingStatus` |  |
| `processing` | Yes | `ListingProcessResult` |  |

## class ListingToAsset

- Source: `src/listing/entities/listingToAsset.entity.ts:16`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `listingToAssetId` | Yes | `number` | `@PrimaryGeneratedColumn({ name: 'listing_to_asset_id' })` |
| `listingId` | Yes | `string` | `@Column({ name: 'listing_id' })` |
| `listing` | Yes | `Listing` | `@ManyToOne(() => Listing, (listing) => listing.listingToAssets)`<br>`@JoinColumn({ name: 'listing_id', referencedColumnName: 'listingId' })` |
| `assetId` | Yes | `string` | `@Column('uuid', { name: 'asset_id' })` |
| `asset` | Yes | `Asset` | `@ManyToOne(() => Asset, (asset) => asset.listingToAssets)`<br>`@JoinColumn({ name: 'asset_id', referencedColumnName: 'assetId' })` |
| `createdAt` | Yes | `Date` | `@CreateDateColumn({ name: 'created_at' })` |
| `updatedAt` | Yes | `Date` | `@UpdateDateColumn({ name: 'updated_at' })` |
| `deletedAt` | Yes | `Date` | `@DeleteDateColumn({ name: 'deleted_at' })` |

## class ListingToSubcategory

- Source: `src/listing/entities/listingToSubcategory.entity.ts:16`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `listingToSubcategoryId` | Yes | `number` | `@PrimaryGeneratedColumn({ name: 'listing_to_subcategory_id' })` |
| `listingId` | Yes | `string` | `@Column({ name: 'listing_id' })` |
| `listing` | Yes | `Listing` | `@ManyToOne(() => Listing, (listing) => listing.listingToSubcategories)`<br>`@JoinColumn({ name: 'listing_id', referencedColumnName: 'listingId' })` |
| `subcategoryId` | Yes | `number` | `@Column('integer', { name: 'subcategory_id' })` |
| `subcategory` | Yes | `Category` | `@ManyToOne(() => Category, (subcategory) => subcategory.listingToSubcategories)`<br>`@JoinColumn({ name: 'subcategory_id', referencedColumnName: 'categoryId' })` |
| `createdAt` | Yes | `Date` | `@CreateDateColumn({ name: 'created_at' })` |
| `updatedAt` | Yes | `Date` | `@UpdateDateColumn({ name: 'updated_at' })` |
| `deletedAt` | Yes | `Date` | `@DeleteDateColumn({ name: 'deleted_at' })` |

## class ListingToTag

- Source: `src/listing/entities/listingToTag.entity.ts:16`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `listingToTagId` | Yes | `number` | `@PrimaryGeneratedColumn({ name: 'listing_to_tag_id' })` |
| `listingId` | Yes | `string` | `@Column({ name: 'listing_id' })` |
| `listing` | Yes | `Listing` | `@ManyToOne(() => Listing, (listing) => listing.listingToTags)`<br>`@JoinColumn({ name: 'listing_id', referencedColumnName: 'listingId' })` |
| `tagId` | Yes | `number` | `@Column('integer', { name: 'tag_id' })` |
| `tag` | Yes | `Tag` | `@ManyToOne(() => Tag, (tag) => tag.listingToTags)`<br>`@JoinColumn({ name: 'tag_id', referencedColumnName: 'tagId' })` |
| `value` | Yes | `string` | `@Column('character varying', { name: 'value', nullable: true })` |
| `createdAt` | Yes | `Date` | `@CreateDateColumn({ name: 'created_at' })` |
| `updatedAt` | Yes | `Date` | `@UpdateDateColumn({ name: 'updated_at' })` |
| `deletedAt` | Yes | `Date` | `@DeleteDateColumn({ name: 'deleted_at' })` |

## class MarketplaceFolderSearchDto

- Source: `src/agent/dto/marketplace-search.dto.ts:99`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `q` | No | `string` | `@IsOptional`<br>`@IsString` |
| `type` | No | `FolderType` | `@IsOptional`<br>`@IsEnum(FolderType)` |
| `media_type` | No | `string` | `@IsOptional`<br>`@IsString` |
| `owner_username` | No | `string` | `@IsOptional`<br>`@IsString` |
| `sort` | No | `string` | `@IsOptional`<br>`@IsString`<br>`@IsIn(['viral_score', 'listing_count', 'created_at', 'child_last_updated_at'])` |
| `page` | No | `number` | `@IsOptional`<br>`@Type(() => Number)`<br>`@IsInt`<br>`@Min(1)` |
| `limit` | No | `number` | `@IsOptional`<br>`@Type(() => Number)`<br>`@IsInt`<br>`@Min(1)`<br>`@Max(100)` |

## class MarketplaceListingDetailDto

- Source: `src/agent/dto/marketplace-search.dto.ts:79`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `by` | No | `string` | `@IsOptional`<br>`@IsString`<br>`@IsIn(['slug', 'name'])` |

## class MarketplaceSearchDto

- Source: `src/agent/dto/marketplace-search.dto.ts:15`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `q` | No | `string` | `@IsOptional`<br>`@IsString` |
| `category` | No | `string` | `@IsOptional`<br>`@IsString` |
| `contract_type` | No | `string` | `@IsOptional`<br>`@IsString` |
| `owner_username` | No | `string` | `@IsOptional`<br>`@IsString` |
| `sort` | No | `string` | `@IsOptional`<br>`@IsString`<br>`@IsIn([ 'newest', 'oldest', 'price_asc', 'price_desc', 'trending', 'most_popular', 'viral_score', ])` |
| `price_min` | No | `number` | `@IsOptional`<br>`@Type(() => Number)`<br>`@IsNumber`<br>`@Min(0)` |
| `price_max` | No | `number` | `@IsOptional`<br>`@Type(() => Number)`<br>`@IsNumber`<br>`@Min(0)` |
| `status` | No | `string` | `@IsOptional`<br>`@IsString` |
| `payment_method` | No | `string` | `@IsOptional`<br>`@IsString` |
| `page` | No | `number` | `@IsOptional`<br>`@Type(() => Number)`<br>`@IsInt`<br>`@Min(1)` |
| `limit` | No | `number` | `@IsOptional`<br>`@Type(() => Number)`<br>`@IsInt`<br>`@Min(1)`<br>`@Max(100)` |

## class MarketplaceUserSearchDto

- Source: `src/agent/dto/marketplace-search.dto.ts:86`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `q` | Yes | `string` | `@IsString`<br>`@MinLength(2)` |
| `limit` | No | `number` | `@IsOptional`<br>`@Type(() => Number)`<br>`@IsInt`<br>`@Min(1)`<br>`@Max(50)` |

## class Mention

- Source: `src/mention/entities/mention.entity.ts:14`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `id` | Yes | `string` | `@PrimaryGeneratedColumn('uuid', { name: 'id' })` |
| `commentId` | Yes | `string` | `@Column({ name: 'comment_id' })` |
| `comment` | Yes | `Comment` | `@ManyToOne(() => Comment, { onDelete: 'CASCADE' })`<br>`@JoinColumn({ name: 'comment_id', referencedColumnName: 'commentId' })` |
| `userId` | Yes | `string` | `@Column({ name: 'user_id' })` |
| `user` | Yes | `User` | `@ManyToOne(() => User)`<br>`@JoinColumn({ name: 'user_id', referencedColumnName: 'userId' })` |
| `read` | Yes | `boolean` | `@Column({ default: false })` |
| `createdAt` | Yes | `Date` | `@CreateDateColumn({ name: 'created_at' })` |

## class MentionDTO

- Source: `src/mention/dto/mention.dto.ts:6`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `id` | Yes | `string` |  |
| `comment` | No | `CommentDTO` |  |
| `listing` | No | `ListingDTO` |  |
| `mentionedBy` | No | `PublicUser` |  |
| `createdAt` | Yes | `Date` |  |
| `read` | Yes | `boolean` |  |

## class MoveListingDto

- Source: `src/folder/dto/move-listing.dto.ts:3`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `targetFolderId` | Yes | `string` | `@IsUUID` |

## class NetworkResponse

- Source: `src/agent/dto/social-engagement.dto.ts:93`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `followers_count` | Yes | `number` |  |
| `following_count` | Yes | `number` |  |

## type NormalizedActivityRow

- Source: `src/agent/services/agent-activity-formatter.service.ts:41`
- Type: `ActivityRow & { details: Record<string, unknown>; }`

## class Notification

- Source: `src/notifications/entities/notification.entity.ts:17`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `notificationId` | Yes | `string` | `@PrimaryGeneratedColumn('uuid', { name: 'notification_id' })` |
| `userId` | Yes | `string` | `@Column({ name: 'user_id' })` |
| `user` | Yes | `User` | `@ManyToOne(() => User, (user) => user.notifications)`<br>`@JoinColumn({ name: 'user_id', referencedColumnName: 'userId' })` |
| `title` | Yes | `string` | `@Column('character varying', { length: 250 })` |
| `message` | Yes | `string` | `@Column('character varying', { length: 1000 })` |
| `link` | Yes | `string` | `@Column('character varying', { nullable: true })` |
| `status` | No | `NotificationStatusType` | `@Column({ type: 'enum', enum: NotificationStatusType, default: NotificationStatusType.NEW, })` |
| `channel` | Yes | `string` | `@Column({ type: 'varchar', length: 20, nullable: true })` |
| `notificationType` | Yes | `string` | `@Column({ type: 'varchar', length: 100, nullable: true, name: 'notification_type', })` |
| `dedupBucketKey` | Yes | `string` | `@Column({ type: 'varchar', length: 500, nullable: true, name: 'dedup_bucket_key', })` |
| `createdAt` | Yes | `Date` | `@CreateDateColumn({ name: 'created_at' })` |
| `updatedAt` | Yes | `Date` | `@UpdateDateColumn({ name: 'updated_at' })` |
| `deletedAt` | Yes | `Date` | `@DeleteDateColumn({ name: 'deleted_at' })` |

## enum NotificationCategoryType

- Source: `src/utils/types.ts:70`

| Member | Value |
|---|---|
| `EMAIL` | `'email'` |
| `WS` | `'ws'` |

## enum NotificationChannel

- Source: `src/notifications/types/notification-channel.enum.ts:1`

| Member | Value |
|---|---|
| `EMAIL` | `'email'` |
| `WS` | `'ws'` |
| `TELEGRAM` | `'telegram'` |
| `IN_APP` | `'in_app'` |

## class NotificationReponseWithTotalDTO

- Source: `src/notifications/dto/notificationReponseWithTotalDTO.ts:4`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `notifications` | Yes | `Notification[]` |  |
| `total` | Yes | `number` |  |

## class NotificationSetting

- Source: `src/user/entities/notificationSetting.entity.ts:18`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `notificationId` | Yes | `string` | `@PrimaryGeneratedColumn('uuid', { name: 'notification_id' })` |
| `userId` | Yes | `string` | `@Column({ name: 'user_id' })` |
| `user` | Yes | `User` | `@ManyToOne(() => User, (user) => user.notificationSettings)`<br>`@JoinColumn([{ name: 'user_id', referencedColumnName: 'userId' }])` |
| `notificationTypeId` | Yes | `number` | `@Column({ name: 'notification_type_id' })` |
| `notificationType` | Yes | `NotificationType` | `@ManyToOne(() => NotificationType, (notificationType) => notificationType.notificationSettings)`<br>`@JoinColumn([ { name: 'notification_type_id', referencedColumnName: 'notificationTypeId', }, ])` |
| `channel` | Yes | `string` | `@Column('varchar', { length: 20, default: NotificationChannel.EMAIL })` |
| `createdAt` | Yes | `Date` | `@CreateDateColumn({ name: 'created_at' })` |
| `updatedAt` | Yes | `Date` | `@UpdateDateColumn({ name: 'updated_at' })` |
| `deletedAt` | Yes | `Date` | `@DeleteDateColumn({ name: 'deleted_at' })` |

## class NotificationsQueryDto

- Source: `src/agent/dto/account.dto.ts:34`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `first` | No | `number` | `@IsOptional`<br>`@Type(() => Number)`<br>`@IsInt`<br>`@Min(1)`<br>`@Max(50)` |
| `limit` | No | `number` | `@IsOptional`<br>`@Type(() => Number)`<br>`@IsInt`<br>`@Min(1)`<br>`@Max(50)` |
| `after` | No | `string` | `@IsOptional`<br>`@IsString` |
| `include_viewed` | No | `boolean` | `@IsOptional`<br>`@Transform(({ value }) => value === 'true' \|\| value === true)`<br>`@IsBoolean` |
| `category` | No | `string` | `@IsOptional`<br>`@IsString`<br>`@IsIn(['social', 'marketplace'])` |

## enum NotificationStatusType

- Source: `src/utils/types.ts:65`

| Member | Value |
|---|---|
| `NEW` | `'new'` |
| `VIEWED` | `'viewed'` |

## interface NotificationTransport

- Source: `src/notifications/transports/notification-transport.interface.ts:5`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `channel` | Yes | `NotificationChannel` |  |

## type NotificationType

- Source: `src/notifications/types/notification-type-registry.ts:48`
- Type: `(typeof NOTIFICATION_TYPES)[keyof typeof NOTIFICATION_TYPES]`

## class NotificationType

- Source: `src/user/entities/notificationType.entity.ts:13`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `notificationTypeId` | Yes | `number` | `@PrimaryGeneratedColumn({ type: 'integer', name: 'notification_type_id' })` |
| `name` | Yes | `string` | `@Column('character varying', { name: 'name' })` |
| `notificationSettings` | Yes | `NotificationSetting[]` | `@OneToMany(() => NotificationSetting, (notificationSettings) => notificationSettings.notificationType)` |
| `createdAt` | Yes | `Date` | `@CreateDateColumn({ name: 'created_at' })` |
| `updatedAt` | Yes | `Date` | `@UpdateDateColumn({ name: 'updated_at' })` |
| `deletedAt` | Yes | `Date` | `@DeleteDateColumn({ name: 'deleted_at' })` |

## class Offer

- Source: `src/marketplace/entities/offer.entity.ts:17`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `offerId` | Yes | `string` | `@PrimaryGeneratedColumn('uuid', { name: 'offer_id' })` |
| `listingId` | Yes | `string` | `@Column({ name: 'listing_id' })` |
| `listing` | Yes | `Listing` | `@ManyToOne(() => Listing, (listing) => listing.offers)`<br>`@JoinColumn({ name: 'listing_id', referencedColumnName: 'listingId' })` |
| `creatorId` | Yes | `string` | `@Column({ name: 'creator_id' })` |
| `creator` | Yes | `User` | `@ManyToOne(() => User, (creator) => creator.offers)`<br>`@JoinColumn({ name: 'creator_id', referencedColumnName: 'userId' })` |
| `price` | Yes | `number` | `@Column('float')` |
| `blockNumber` | Yes | `number` | `@Column('bigint', { name: 'block_number' })` |
| `paymentToken` | Yes | `string` | `@Column('character varying', { name: 'payment_token', nullable: true })` |
| `deadline` | Yes | `Date` | `@Column({ type: 'timestamptz' })` |
| `paymentId` | Yes | `string` | `@Column('character varying', { name: 'payment_id', nullable: true })` |
| `status` | Yes | `OfferStatus` | `@Column({ type: 'enum', enum: OfferStatus, default: OfferStatus.CREATED, })` |
| `counterPrice` | Yes | `number` | `@Column({ name: 'counter_price', type: 'float', nullable: true })` |
| `counterDeadline` | Yes | `Date` | `@Column({ name: 'counter_deadline', type: 'timestamptz', nullable: true })` |
| `parentOfferId` | Yes | `string` | `@Column({ name: 'parent_offer_id', type: 'uuid', nullable: true })` |
| `parentOffer` | Yes | `Offer` | `@ManyToOne(() => Offer, { nullable: true })`<br>`@JoinColumn({ name: 'parent_offer_id' })` |
| `counterRounds` | Yes | `number` | `@Column({ name: 'counter_rounds', type: 'int', default: 0 })` |
| `createdAt` | Yes | `Date` | `@CreateDateColumn({ name: 'created_at' })` |
| `updatedAt` | Yes | `Date` | `@UpdateDateColumn({ name: 'updated_at' })` |
| `deletedAt` | Yes | `Date` | `@DeleteDateColumn({ name: 'deleted_at' })` |

## class OfferCanceledDTO

- Source: `src/marketplace/dto/offerCanceled.dto.ts:4`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `transactionHash` | Yes | `string` | `@IsString` |
| `blockNumber` | Yes | `number` | `@IsNumber` |
| `creatorC` | Yes | `string` | `@IsEthereumAddress` |
| `tokenId` | Yes | `number` | `@IsNumber` |

## class OfferCreatedDTO

- Source: `src/marketplace/dto/offerCreated.dto.ts:4`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `transactionHash` | Yes | `string` | `@IsString` |
| `blockNumber` | Yes | `number` | `@IsNumber` |
| `creatorC` | Yes | `string` | `@IsEthereumAddress` |
| `tokenId` | Yes | `number` | `@IsNumber` |
| `pricePerItem` | Yes | `string` | `@IsString` |
| `deadline` | Yes | `string` | `@IsString` |

## class OfferDTO

- Source: `src/marketplace/dto/offer.dto.ts:6`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `offerId` | Yes | `string` |  |
| `listingId` | Yes | `string` |  |
| `listing` | Yes | `ListingDTO` |  |
| `creatorId` | Yes | `string` |  |
| `creator` | Yes | `PublicUser` |  |
| `price` | Yes | `number` |  |
| `blockNumber` | Yes | `number` |  |
| `paymentToken` | Yes | `string` |  |
| `deadline` | No | `Date` |  |
| `isExpired` | Yes | `boolean` |  |
| `createdAt` | No | `Date` |  |
| `counterPrice` | Yes | `number` |  |
| `counterDeadline` | Yes | `Date` |  |
| `parentOfferId` | Yes | `string` |  |
| `status` | Yes | `string` |  |

## class OfferPeriodQueryDto

- Source: `src/agent/dto/offer.dto.ts:48`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `period` | No | `'day' \| 'week' \| 'month' \| 'year'` | `@IsOptional`<br>`@IsString` |

## class OffersResponseDTO

- Source: `src/marketplace/dto/offersResponse.dto.ts:5`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `offers` | Yes | `OfferDTO[]` |  |
| `totalOffers` | Yes | `ItemsByDateDTO[]` |  |
| `lifetimeOffers` | Yes | `ItemsByDateDTO[]` |  |
| `totalGrowth` | Yes | `number` |  |
| `lifetimeGrowth` | Yes | `number` |  |

## enum OfferStatus

- Source: `src/marketplace/utils/offerStatus.ts:1`

| Member | Value |
|---|---|
| `CREATING` | `'CREATING'` |
| `CREATED` | `'CREATED'` |
| `CANCELING` | `'CANCELING'` |
| `REJECTING` | `'REJECTING'` |
| `COUNTERED` | `'COUNTERED'` |

## class OffersTotalDTO

- Source: `src/marketplace/dto/offersTotal.dto.ts:3`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `receivedOffers` | Yes | `number` |  |
| `sentOffers` | Yes | `number` |  |

## class OfferTransferDTO

- Source: `src/marketplace/dto/offerTransfer.dto.ts:5`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `transactionHash` | Yes | `string` | `@IsString` |
| `price` | Yes | `number` | `@IsNumber` |
| `offererC` | Yes | `string` | `@IsString` |
| `receiverC` | Yes | `string` | `@IsString` |
| `tokenId` | Yes | `number` | `@IsNumber` |
| `blockNumber` | No | `number` | `@IsNumber`<br>`@IsOptional` |

## type OperatorRow

- Source: `src/agent/services/agent-operator-resolver.service.ts:4`
- Type: `{ operator_id: string }`

## interface OpsAlertNotification

- Source: `src/notifications/types/ops-alert-notification.interface.ts:3`

_No declared properties._

## interface OutboxConfig
_Max retries before dead letter. Default: 10_

- Source: `src/resilience/outbox/outbox.types.ts:19`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `maxRetries` | No | `number` |  |
| `baseDelay` | No | `number` |  |
| `staleThreshold` | No | `number` |  |
| `batchSize` | No | `number` |  |

## class OutboxEntry

- Source: `src/resilience/outbox/outbox.entity.ts:10`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `id` | Yes | `string` | `@PrimaryGeneratedColumn('uuid')` |
| `eventType` | Yes | `string` | `@Column({ name: 'event_type', type: 'varchar' })` |
| `payload` | Yes | `Record<string, any>` | `@Column({ type: 'jsonb' })` |
| `idempotencyKey` | Yes | `string` | `@Column({ name: 'idempotency_key', type: 'varchar' })` |
| `status` | Yes | `string` | `@Column({ type: 'varchar', default: 'pending' })` |
| `retryCount` | Yes | `number` | `@Column({ name: 'retry_count', type: 'int', default: 0 })` |
| `nextRetryAt` | Yes | `Date` | `@Column({ name: 'next_retry_at', type: 'timestamptz', default: () => 'NOW()', })` |
| `result` | Yes | `Record<string, any> \| null` | `@Column({ type: 'jsonb', nullable: true })` |
| `createdAt` | Yes | `Date` | `@CreateDateColumn({ name: 'created_at', type: 'timestamptz' })` |
| `updatedAt` | Yes | `Date` | `@UpdateDateColumn({ name: 'updated_at', type: 'timestamptz' })` |

## class OutboxEntryDTO

- Source: `src/resilience/outbox/outbox-entry.dto.ts:3`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `id` | Yes | `string` |  |
| `eventType` | Yes | `string` |  |
| `payload` | Yes | `string` |  |
| `idempotencyKey` | Yes | `string` |  |
| `status` | Yes | `string` |  |
| `retryCount` | Yes | `number` |  |
| `nextRetryAt` | Yes | `Date` |  |
| `result` | Yes | `string` |  |
| `createdAt` | Yes | `Date` |  |
| `updatedAt` | Yes | `Date` |  |

## type OutboxHandler

- Source: `src/resilience/outbox/outbox.types.ts:9`
- Type: `( payload: Record<string, any>, idempotencyKey: string, ) => Promise<Record<string, any>>`

## enum OutboxStatus

- Source: `src/resilience/outbox/outbox.types.ts:1`

| Member | Value |
|---|---|
| `PENDING` | `'pending'` |
| `PROCESSING` | `'processing'` |
| `COMPLETED` | `'completed'` |
| `FAILED` | `'failed'` |
| `DEAD_LETTER` | `'dead_letter'` |

## class OverageDTO

- Source: `src/billing/dto/billing.dto.ts:56`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `allowed` | Yes | `boolean` |  |
| `capCents` | Yes | `number \| null` |  |

## class PageInfo

- Source: `src/search/dto/cursor-pagination.dto.ts:3`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `hasNextPage` | Yes | `boolean` |  |
| `endCursor` | No | `string` |  |

## class PaginatedComments

- Source: `src/activity/dto/paginated-comments.dto.ts:5`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `comments` | Yes | `CommentDTO[]` |  |
| `pageInfo` | Yes | `PageInfo` |  |
| `totalCount` | Yes | `number` |  |

## class PaginatedFolderListings

- Source: `src/folder/dto/paginated-folder-listings.dto.ts:16`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `items` | Yes | `FolderListingEdge[]` |  |
| `nextCursor` | No | `string` |  |
| `hasMore` | Yes | `boolean` |  |

## class PaginatedFoldersSearchResult

- Source: `src/search/dto/paginated-folders-search-result.dto.ts:4`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `folders` | Yes | `FolderSearchCard[]` |  |
| `total` | Yes | `number` |  |
| `page` | Yes | `number` |  |
| `perPage` | Yes | `number` |  |

## class PaginatedListings

- Source: `src/search/dto/paginated-listings.dto.ts:5`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `listings` | Yes | `ListingDTO[]` |  |
| `pageInfo` | Yes | `PageInfo` |  |
| `totalCount` | Yes | `number` |  |

## class PaginatedListingsDTO

- Source: `src/listing/dto/paginated-listings.dto.ts:4`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `listings` | Yes | `ListingDTO[]` |  |
| `nextCursor` | No | `string` |  |
| `hasMore` | Yes | `boolean` |  |

## class PaginatedNotifications

- Source: `src/notifications/dto/paginated-notifications.dto.ts:5`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `notifications` | Yes | `Notification[]` |  |
| `pageInfo` | Yes | `PageInfo` |  |
| `totalCount` | Yes | `number` |  |

## type ParentListingRow

- Source: `src/user-feed-queue/services/feed-target-hydration.service.ts:27`
- Type: `{ assetId: string; listingId: string; listingName: string \| null; listingDescription: string \| null; }`

## class PasswordSetDto

- Source: `src/agent/dto/password-set.dto.ts:7`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `password` | Yes | `string` | `@IsStrongPassword(IS_STRONG_PASSWORD_OPTIONS)`<br>`@MaxLength(PASSWORD_RULES.maxLength)` |

## interface PayPalErrorInfo

- Source: `src/paypal/paypal-errors.ts:24`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `status` | Yes | `number` |  |
| `issue` | Yes | `string \| undefined` |  |
| `description` | Yes | `string \| undefined` |  |
| `name` | Yes | `string` |  |

## class PayPalMerchantDTO

- Source: `src/paypal/dto/paypalMerchant.dto.ts:3`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `merchant_id` | Yes | `string` |  |
| `tracking_id` | Yes | `string` |  |
| `payments_receivable` | Yes | `boolean` |  |
| `legal_name` | Yes | `string` |  |
| `primary_email_confirmed` | Yes | `string` |  |

## class PayPalOnboardingStatusDTO

- Source: `src/paypal/dto/paypalOnboardingStatus.dto.ts:3`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `status` | Yes | `string` |  |
| `paymentsReceivable` | Yes | `boolean` |  |
| `emailConfirmed` | Yes | `boolean` |  |
| `vettingStatus` | No | `string` |  |

## class PayPalSession

- Source: `src/paypal/entities/paypalSession.entity.ts:11`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `paypalSessionId` | Yes | `string` | `@PrimaryGeneratedColumn('uuid', { name: 'paypal_session_id' })` |
| `buyerId` | Yes | `string` | `@Column({ name: 'buyer_id' })` |
| `listingId` | Yes | `string` | `@Column({ name: 'listing_id' })` |
| `sellerId` | Yes | `string` | `@Column({ name: 'seller_id' })` |
| `orderId` | Yes | `string` | `@Column({ name: 'order_id', nullable: true })` |
| `refId` | Yes | `string` | `@Column({ name: 'ref_id', nullable: true })` |
| `failed` | Yes | `boolean` | `@Column('boolean', { nullable: true })` |
| `released` | Yes | `boolean` | `@Column('boolean', { nullable: true })` |
| `eventDetails` | Yes | `string` | `@Column('json', { name: 'event_details', nullable: true })` |
| `success` | Yes | `string` | `@Column('json', { name: 'success', nullable: true })` |
| `type` | No | `PurchaseSessionType` | `@Column({ type: 'enum', enum: PurchaseSessionType, nullable: true })` |
| `deadline` | Yes | `Date` | `@Column({ type: 'timestamptz', nullable: true })` |
| `createdAt` | Yes | `Date` | `@CreateDateColumn({ name: 'created_at' })` |

## class PayPalSetupQueryDto

- Source: `src/agent/dto/setup-paypal.dto.ts:17`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `intent` | Yes | `'vault_only' \| 'full_seller'` | `@IsOptional`<br>`@IsIn(['vault_only', 'full_seller'])` |

## class PaypalSetupToken

- Source: `src/agent/entities/paypal-setup-token.entity.ts:12`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `state` | Yes | `string` | `@PrimaryColumn({ type: 'varchar', length: 64 })` |
| `agentId` | Yes | `string` | `@Column({ name: 'agent_id', type: 'uuid' })` |
| `setupTokenId` | Yes | `string` | `@Column({ name: 'setup_token_id', type: 'varchar', length: 64 })` |
| `createdAt` | Yes | `Date` | `@CreateDateColumn({ name: 'created_at', type: 'timestamptz' })` |
| `expiresAt` | Yes | `Date` | `@Index`<br>`@Column({ name: 'expires_at', type: 'timestamptz' })` |
| `partnerReferralUrl` | Yes | `string \| null` | `@Column({ name: 'partner_referral_url', type: 'varchar', length: 2048, nullable: true })` |
| `intent` | Yes | `string` | `@Column({ type: 'varchar', length: 16, default: 'full_seller' })` |
| `agent` | Yes | `User` | `@ManyToOne(() => User)`<br>`@JoinColumn({ name: 'agent_id' })` |

## class PayToken

- Source: `src/listing/entities/payToken.entity.ts:19`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `payTokenId` | Yes | `number` | `@PrimaryGeneratedColumn({ type: 'integer', name: 'pay_token_id' })` |
| `name` | Yes | `string` | `@Column('character varying', { name: 'name' })` |
| `icon` | Yes | `string` | `@Column('character varying', { name: 'icon', nullable: true })` |
| `symbol` | Yes | `string` | `@Column('character varying', { name: 'symbol' })` |
| `address` | Yes | `string` | `@Column('character varying', { name: 'address' })` |
| `chainlinkProxyAddress` | Yes | `string` | `@Column('character varying', { name: 'chainlink_proxy_address', nullable: true, })` |
| `decimals` | Yes | `number` | `@Column('integer', { name: 'decimals' })` |
| `price` | Yes | `number` | `@Column('float', { name: 'price', default: 0 })` |
| `isMainnet` | Yes | `boolean` | `@Column({ name: 'is_mainnet', default: true })` |
| `isDisabled` | Yes | `boolean` | `@Column({ name: 'is_disabled', default: false })` |
| `listings` | Yes | `Listing[]` | `@OneToMany(() => Listing, (listings) => listings.payToken)` |
| `userId` | Yes | `string` | `@Column({ name: 'user_id', nullable: true })` |
| `user` | Yes | `User` | `@ManyToOne(() => User, (user) => user.payTokens)`<br>`@JoinColumn({ name: 'user_id', referencedColumnName: 'userId' })` |
| `community` | Yes | `Record<string, any>` | `@Column('jsonb', { name: 'community', nullable: true })` |
| `txHash` | Yes | `string` | `@Column('character varying', { name: 'tx_hash', nullable: true })` |
| `status` | No | `TokenStatus` | `@Column({ type: 'enum', enum: TokenStatus, nullable: true })` |
| `createdAt` | Yes | `Date` | `@CreateDateColumn({ name: 'created_at' })` |
| `updatedAt` | Yes | `Date` | `@UpdateDateColumn({ name: 'updated_at' })` |
| `deletedAt` | Yes | `Date` | `@DeleteDateColumn({ name: 'deleted_at' })` |

## class PayTokenResponseWithTotalDTO

- Source: `src/listing/dto/payTokenResponseWithTotal.dto.ts:4`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `payTokens` | Yes | `PayToken[]` |  |
| `total` | Yes | `number` |  |

## interface PendingEvent

- Source: `src/search/folder-search-sync.subscriber.ts:23`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `folderId` | Yes | `string` |  |
| `eventType` | Yes | `FolderEventType` |  |

## class PeriodAllQueryDto

- Source: `src/agent/dto/analytics-query.dto.ts:10`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `period` | No | `string` | `@IsOptional`<br>`@IsIn(['7d', '30d', '90d', 'all'])` |

## class PeriodQueryDto

- Source: `src/agent/dto/analytics-query.dto.ts:4`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `period` | No | `string` | `@IsOptional`<br>`@IsIn(['7d', '30d', '90d'])` |

## class PeriodSortLimitQueryDto

- Source: `src/agent/dto/analytics-query.dto.ts:64`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `period` | No | `string` | `@IsOptional`<br>`@IsIn(['7d', '30d', '90d'])` |
| `sort_by` | No | `string` | `@IsOptional`<br>`@IsIn(['volume', 'revenue'])` |
| `limit` | No | `number` | `@IsOptional`<br>`@Type(() => Number)`<br>`@IsInt`<br>`@Min(1)`<br>`@Max(50)` |

## type PeriodType

- Source: `src/utils/types.ts:11`
- Type: `'day' \| 'week' \| 'month' \| 'year'`

## type PeriodUnit

- Source: `src/utils/generalHelper.ts:318`
- Type: `'day' \| 'days' \| 'week' \| 'weeks' \| 'month' \| 'months' \| 'year' \| 'years' \| 'minutes'`

## enum PermissionAction

- Source: `src/permissions/utils/types.ts:7`

| Member | Value |
|---|---|
| `SHOW_VERIFIED_BADGE` | `'show_verified_badge'` |
| `CUSTOM_AVATAR_BORDER` | `'custom_avatar_border'` |
| `PROFILE_TITLE` | `'profile_title'` |
| `SHOW_REWARDS` | `'show_rewards'` |
| `DOWNLOAD_ASSETS` | `'download_assets'` |
| `MAKE_OFFERS` | `'make_offers'` |
| `FILTER_OFFERS` | `'filter_offers'` |
| `VIEW_TX_HISTORY` | `'view_tx_history'` |
| `VIEW_VIRAL_SCORE` | `'view_viral_score'` |
| `ACCESS_AI_TOOLS` | `'access_ai_tools'` |
| `REPORT_ASSET` | `'report_asset'` |
| `VIEW_PROMPTS` | `'view_prompts'` |
| `MAX_INVITES` | `'max_invites'` |
| `HIDE_ADS` | `'hide_ads'` |
| `SHOW_AVATAR_ON_LISTINGS` | `'show_avatar_on_listings'` |
| `MAKE_PRIVATE` | `'make_private'` |

## enum PermissionScope

- Source: `src/permissions/utils/types.ts:1`

| Member | Value |
|---|---|
| `NONE` | `'NONE'` |
| `OWNED_ONLY` | `'OWNED_ONLY'` |
| `ALL` | `'ALL'` |

## class PlaceBidDto

- Source: `src/agent/dto/auction.dto.ts:4`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `amount` | Yes | `number` | `@IsNumber`<br>`@IsPositive` |
| `payment_id` | No | `string` | `@IsOptional`<br>`@IsString` |

## class PlanDTO

- Source: `src/billing/dto/billing.dto.ts:104`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `code` | Yes | `string` |  |
| `name` | Yes | `string` |  |
| `description` | Yes | `string` |  |
| `features` | Yes | `string[]` |  |
| `priceMonthly` | Yes | `number` |  |
| `priceYearly` | Yes | `number` |  |
| `currency` | Yes | `string` |  |
| `creditsMonthly` | Yes | `number` |  |
| `agentSlots` | Yes | `number` |  |
| `maxPortfolios` | Yes | `number` |  |
| `maxCollections` | Yes | `number` |  |

## class PlanSelectionDto

- Source: `src/agent/dto/account.dto.ts:70`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `plan` | Yes | `string` | `@Transform(({ value }) => value?.trim().toLowerCase())`<br>`@IsIn(['unleashed', 'genesis'])` |

## class PointEarned

- Source: `src/point/entities/pointEarned.entity.ts:15`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `pointEarnedId` | Yes | `string` | `@PrimaryGeneratedColumn('uuid', { name: 'point_earned_id' })` |
| `userId` | Yes | `string` | `@Column({ name: 'userId' })` |
| `user` | Yes | `User` | `@ManyToOne(() => User, (user) => user.pointEarned)`<br>`@JoinColumn([{ name: 'userId', referencedColumnName: 'userId' }])` |
| `pointType` | Yes | `string` | `@Column('character varying', { name: 'reward_type' })` |
| `amount` | Yes | `number` | `@Column({ type: 'float' })` |
| `objectId` | Yes | `string` | `@Column({ name: 'object_id', nullable: true })` |
| `createdAt` | Yes | `Date` | `@CreateDateColumn({ name: 'created_at' })` |
| `updatedAt` | Yes | `Date` | `@UpdateDateColumn({ name: 'updated_at' })` |
| `deletedAt` | Yes | `Date` | `@DeleteDateColumn({ name: 'deleted_at' })` |

## class PointRedeemed

- Source: `src/point/entities/pointRedeemed.entity.ts:15`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `pointRedeemedId` | Yes | `string` | `@PrimaryGeneratedColumn('uuid', { name: 'point_redeemed_id' })` |
| `userId` | Yes | `string` | `@Column({ name: 'userId' })` |
| `user` | Yes | `User` | `@ManyToOne(() => User, (user) => user.pointRedeemed)`<br>`@JoinColumn([{ name: 'userId', referencedColumnName: 'userId' }])` |
| `amount` | Yes | `number` | `@Column({ type: 'float', name: 'amount' })` |
| `txHash` | Yes | `string` | `@Column({ name: 'tx_hash', nullable: true })` |
| `createdAt` | Yes | `Date` | `@CreateDateColumn({ name: 'created_at' })` |
| `updatedAt` | Yes | `Date` | `@UpdateDateColumn({ name: 'updated_at' })` |
| `deletedAt` | Yes | `Date` | `@DeleteDateColumn({ name: 'deleted_at' })` |

## class PointResponseDTO

- Source: `src/point/dto/rewardsResponse.dto.ts:5`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `pointEarned` | Yes | `PointEarned[]` |  |
| `totalPointEarned` | Yes | `ItemsByDateDTO[]` |  |
| `lifetimePointEarned` | Yes | `ItemsByDateDTO[]` |  |
| `totalGrowth` | Yes | `number` |  |
| `lifetimeGrowth` | Yes | `number` |  |

## class PointsBalanceDTO

- Source: `src/point/dto/points-balance.dto.ts:3`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `total` | Yes | `number` |  |
| `lifetimeEarned` | Yes | `number` |  |

## class PointsHistoryQueryDto

- Source: `src/agent/dto/account.dto.ts:28`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `period` | No | `string` | `@IsOptional`<br>`@IsString` |

## class PointType

- Source: `src/point/entities/pointType.entity.ts:12`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `pointTypeId` | Yes | `number` | `@PrimaryGeneratedColumn({ name: 'point_type_id' })` |
| `symbol` | Yes | `string` | `@Column('character varying', { name: 'symbol' })` |
| `name` | Yes | `string` | `@Column('character varying', { name: 'name' })` |
| `description` | Yes | `string` | `@Column('character varying', { name: 'description', default: null })` |
| `amount` | Yes | `number` | `@Column('integer', { name: 'amount' })` |
| `referrerAmount` | Yes | `number` | `@Column('integer', { name: 'referrer_amount', default: 0 })` |
| `grandReferrerAmount` | Yes | `number` | `@Column('integer', { name: 'grand_referrer_amount', default: 0 })` |
| `createdAt` | Yes | `Date` | `@CreateDateColumn({ name: 'created_at' })` |
| `updatedAt` | Yes | `Date` | `@UpdateDateColumn({ name: 'updated_at' })` |
| `deletedAt` | Yes | `Date` | `@DeleteDateColumn({ name: 'deleted_at' })` |

## class PointTypeDTO

- Source: `src/point/dto/pointType.dto.ts:4`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `name` | Yes | `string` | `@IsString` |
| `amount` | Yes | `number` | `@IsNumber` |
| `description` | No | `string` | `@IsOptional`<br>`@IsString` |
| `referrerAmount` | No | `number` | `@IsOptional`<br>`@IsNumber` |
| `grandReferrerAmount` | No | `number` | `@IsOptional`<br>`@IsNumber` |

## class PortfolioQueryDto

- Source: `src/agent/dto/marketplace-purchase.dto.ts:92`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `page` | No | `number` | `@IsOptional`<br>`@Type(() => Number)`<br>`@IsNumber`<br>`@Min(1)` |
| `limit` | No | `number` | `@IsOptional`<br>`@Type(() => Number)`<br>`@IsNumber`<br>`@Min(1)`<br>`@Max(50)` |
| `status` | No | `string` | `@IsOptional`<br>`@IsString` |

## interface PostSignupResult

- Source: `src/auth/post-signup.ts:12`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `address` | Yes | `string` |  |
| `referralCode` | Yes | `string` |  |
| `referrerId` | Yes | `string \| null` |  |

## class PriceEventDTO

- Source: `src/analytics/dto/price-history.dto.ts:3`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `eventName` | Yes | `string` |  |
| `price` | Yes | `number` |  |
| `timestamp` | Yes | `Date` |  |
| `txHash` | No | `string` |  |

## class PriceHistoryDTO

- Source: `src/analytics/dto/price-history.dto.ts:18`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `listingId` | Yes | `string` |  |
| `events` | Yes | `PriceEventDTO[]` |  |
| `period` | Yes | `string` |  |

## class PriceMoversQueryDto

- Source: `src/agent/dto/analytics-query.dto.ts:51`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `direction` | No | `'up' \| 'down'` | `@IsOptional`<br>`@IsIn(['up', 'down'])` |
| `limit` | No | `number` | `@IsOptional`<br>`@Type(() => Number)`<br>`@IsInt`<br>`@Min(1)`<br>`@Max(50)` |

## type Primitive

- Source: `src/utils/sanitize-details.ts:28`
- Type: `string \| number \| boolean \| null`

## class PrivateUser

- Source: `src/user/dto/private-user.dto.ts:15`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `email` | Yes | `string` |  |
| `isEmailConfirmed` | Yes | `boolean` |  |
| `isActive` | Yes | `boolean` |  |
| `is2fa` | Yes | `boolean` |  |
| `unredeemedPoint` | Yes | `number` |  |
| `redeemedPoint` | Yes | `number` |  |
| `isPayPalKYCed` | Yes | `boolean` |  |
| `hasPayPalMerchantId` | Yes | `boolean` |  |
| `userWallets` | Yes | `PublicWallet[]` |  |
| `billingSubscription` | Yes | `BillingSubscription` |  |
| `notificationSettings` | Yes | `NotificationSetting[]` |  |
| `whitelistRequests` | Yes | `WhitelistRequest[]` |  |
| `userStatus` | Yes | `UserStatus` |  |
| `isAdmin` | Yes | `boolean` |  |
| `referralCode` | Yes | `string` |  |
| `customInviteQuota` | Yes | `number` |  |

## interface PrivateUserOptions

- Source: `src/user/dto/private-user.dto.ts:11`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `hideCheckedRequests` | No | `boolean` |  |

## class ProfileCountsDTO

- Source: `src/user/dto/profile-counts.dto.ts:3`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `listingsCount` | Yes | `number` |  |
| `privateListingsCount` | No | `number` |  |
| `likesCount` | Yes | `number` |  |
| `favoritesCount` | Yes | `number` |  |
| `receivedOffersCount` | Yes | `number` |  |
| `sentOffersCount` | Yes | `number` |  |
| `bidsCount` | Yes | `number` |  |
| `payTokensCount` | Yes | `number` |  |
| `referralsCount` | Yes | `number` |  |

## class ProfileDashboardDTO

- Source: `src/user/dto/profile-dashboard.dto.ts:3`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `followers` | Yes | `number` |  |
| `followings` | Yes | `number` |  |
| `listingsCount` | Yes | `number` |  |
| `privateListingsCount` | No | `number` |  |
| `likesCount` | Yes | `number` |  |
| `favoritesCount` | Yes | `number` |  |
| `receivedOffersCount` | Yes | `number` |  |
| `sentOffersCount` | Yes | `number` |  |
| `bidsCount` | Yes | `number` |  |
| `payTokensCount` | Yes | `number` |  |
| `referralsCount` | Yes | `number` |  |
| `licensesCount` | No | `number` |  |
| `inviteTokensCount` | No | `number` |  |
| `isFollowing` | No | `boolean` |  |

## type Provider

- Source: `src/resilience/idempotency/idempotent-http.factory.ts:4`
- Type: `'paypal' \| 'stripe' \| 'custom'`

## class PublicUser

- Source: `src/user/dto/public-user.dto.ts:13`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `userId` | Yes | `string` |  |
| `userName` | Yes | `string` |  |
| `name` | Yes | `string` |  |
| `avatar` | Yes | `string` |  |
| `banner` | Yes | `string` |  |
| `bio` | Yes | `string` |  |
| `twitter` | Yes | `string` |  |
| `instagram` | Yes | `string` |  |
| `website` | Yes | `string` |  |
| `creatorStatus` | Yes | `CreatorStatus` |  |
| `isFollowing` | Yes | `boolean` |  |
| `isAgent` | Yes | `boolean` |  |
| `viralScore` | Yes | `number` |  |
| `createdAt` | Yes | `Date` |  |
| `planCode` | Yes | `string` |  |
| `isVip` | Yes | `boolean` |  |

## interface PublicUserOptions

- Source: `src/user/dto/public-user.dto.ts:8`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `followerId` | No | `string` |  |
| `isFollowing` | No | `boolean` |  |

## class PublicWallet

- Source: `src/user/dto/public-wallet.dto.ts:4`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `address` | Yes | `string` |  |
| `isVerified` | Yes | `boolean` |  |

## class PublishListingAgentDto

- Source: `src/agent/dto/marketplace-purchase.dto.ts:62`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `price` | Yes | `number` | `@IsNumber({ maxDecimalPlaces: 2 })`<br>`@Min(0)`<br>`@Type(() => Number)` |
| `payment_method` | No | `string` | `@IsOptional`<br>`@IsString` |

## class PublishListingDTO

- Source: `src/listing/dto/publishListing.dto.ts:5`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `listingId` | Yes | `string` | `@IsString` |
| `price` | Yes | `number` | `@IsNumber` |
| `payTokenAddress` | No | `string` | `@IsOptional`<br>`@IsString` |
| `paymentMethod` | Yes | `ListingPaymentMethod` | `@IsString` |

## class PublishListingResultDTO

- Source: `src/listing/dto/publishListingResult.dto.ts:3`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `message` | Yes | `string` |  |
| `listingId` | No | `string` |  |
| `status` | No | `string` |  |

## class PurchaseListingInput

- Source: `src/listing/dto/purchase-listing.dto.ts:3`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `listingId` | Yes | `string` |  |
| `idempotencyKey` | Yes | `string` |  |
| `transferOwnership` | No | `boolean` |  |

## class PurchaseResultDTO

- Source: `src/listing/dto/purchase-result.dto.ts:3`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `success` | Yes | `boolean` |  |
| `transactionId` | No | `string` |  |
| `status` | No | `string` |  |
| `downloadUrl` | No | `string` |  |
| `message` | No | `string` |  |
| `ownershipTransferred` | No | `boolean` |  |

## enum PurchaseSessionType

- Source: `src/utils/types.ts:90`

| Member | Value |
|---|---|
| `BUY` | `'buy'` |
| `AUTHORIZE` | `'authorize'` |
| `BUY_AUTHORIZE` | `'buy_authorize'` |
| `DOWNLOAD_LICENSE` | `'download_license'` |

## class PurchasesQueryDto

- Source: `src/agent/dto/marketplace-purchase.dto.ts:45`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `page` | No | `number` | `@IsOptional`<br>`@Type(() => Number)`<br>`@IsNumber`<br>`@Min(1)` |
| `limit` | No | `number` | `@IsOptional`<br>`@Type(() => Number)`<br>`@IsNumber`<br>`@Min(1)`<br>`@Max(50)` |

## class PurchaseStatusDTO

- Source: `src/listing/dto/purchase-status.dto.ts:3`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `status` | Yes | `string` |  |
| `transactionId` | No | `string` |  |
| `downloadUrl` | No | `string` |  |
| `message` | No | `string` |  |

## class PurchaseStatusQueryDto

- Source: `src/agent/dto/marketplace-purchase.dto.ts:27`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `idempotency_key` | Yes | `string` | `@IsString`<br>`@IsNotEmpty`<br>`@IsUUID` |

## enum PurchaseType

- Source: `src/utils/types.ts:97`

| Member | Value |
|---|---|
| `OWNERSHIP` | `'ownership'` |
| `DOWNLOAD_LICENSE` | `'download_license'` |

## class QA

- Source: `src/user/entities/qa.entity.ts:14`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `qaId` | Yes | `number` | `@PrimaryGeneratedColumn({ name: 'qa_id' })` |
| `question` | Yes | `string` | `@Column('character varying')` |
| `answer` | Yes | `string` | `@Column('character varying')` |
| `questionTypeId` | Yes | `number` | `@Column({ name: 'question_type_id', nullable: true })` |
| `questionType` | Yes | `QuestionType` | `@ManyToOne(() => QuestionType, (qtype) => qtype.QAs)`<br>`@JoinColumn([ { name: 'question_type_id', referencedColumnName: 'questionTypeId' }, ])` |
| `createdAt` | Yes | `Date` | `@CreateDateColumn({ name: 'created_at' })` |
| `updatedAt` | Yes | `Date` | `@UpdateDateColumn({ name: 'updated_at' })` |
| `deletedAt` | Yes | `Date` | `@DeleteDateColumn({ name: 'deleted_at' })` |

## class QuestionType

- Source: `src/user/entities/questionType.entity.ts:13`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `questionTypeId` | Yes | `number` | `@PrimaryGeneratedColumn({ name: 'question_type_id' })` |
| `type` | Yes | `string` | `@Column('character varying')` |
| `QAs` | Yes | `QA[]` | `@OneToMany(() => QA, (qa) => qa.questionType)` |
| `createdAt` | Yes | `Date` | `@CreateDateColumn({ name: 'created_at' })` |
| `updatedAt` | Yes | `Date` | `@UpdateDateColumn({ name: 'updated_at' })` |
| `deletedAt` | Yes | `Date` | `@DeleteDateColumn({ name: 'deleted_at' })` |

## interface RateLimitResponse

- Source: `src/agent/dto/agent-rate-limit.dto.ts:1`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `requests_per_minute` | Yes | `number` |  |
| `current_usage` | Yes | `number` |  |
| `remaining` | Yes | `number` |  |
| `resets_at` | Yes | `string` |  |

## class RawEventsQueryDto

- Source: `src/agent/dto/raw-events-query.dto.ts:15`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `time_range` | Yes | `string` | `@IsIn(['1h', '6h', '24h', '7d', '30d'])` |
| `event_type` | No | `string[]` | `@IsOptional`<br>`@Transform(({ value }) => typeof value === 'string' ? value.split(',') : value)`<br>`@IsArray`<br>`@ArrayMaxSize(10)`<br>`@IsString({ each: true })` |
| `category` | No | `string` | `@IsOptional`<br>`@IsString` |
| `price_min` | No | `number` | `@IsOptional`<br>`@Type(() => Number)`<br>`@IsNumber`<br>`@Min(0)` |
| `price_max` | No | `number` | `@IsOptional`<br>`@Type(() => Number)`<br>`@IsNumber`<br>`@Min(0)` |
| `listing_id` | No | `string` | `@IsOptional`<br>`@IsUUID` |
| `seller_id` | No | `string` | `@IsOptional`<br>`@IsUUID` |
| `buyer_id` | No | `string` | `@IsOptional`<br>`@IsUUID` |
| `cursor` | No | `string` | `@IsOptional`<br>`@IsString` |
| `limit` | No | `number` | `@IsOptional`<br>`@Type(() => Number)`<br>`@IsInt`<br>`@Min(1)`<br>`@Max(100)` |

## class RecordViewResponse

- Source: `src/agent/dto/social-engagement.dto.ts:81`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `message` | Yes | `string` |  |

## interface Recovery
_Agent-facing fine-grained error code, e.g. `FOLDER_CAP_REACHED`. The existing coarse `error` field (`VALIDATION_ERROR` / `NOT_FOUND` / ...) stays unchanged — `code` is an additive, more-specific signal._

- Source: `src/utils/error-recovery.ts:19`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `code` | No | `string` |  |
| `hint` | No | `string` |  |
| `next` | No | `{ options?: RecoveryOption[]; /** Skill-doc anchor where this error is documented in detail. */ docs?: string; }` |  |

## interface RecoveryOption
_Static recovery metadata attached to agent-facing errors. Lives in a sidecar so `CustomException` / `StaticErrors` remain plain string enums (keeps `graphql-error-codes.ts` unchanged and avoids circular imports). The filter reads this map when emitting a response for a `CustomException`. Entries are optional — static errors without an entry still work; they just don't ship a `code` / `hint` / `next` triple._

- Source: `src/utils/error-recovery.ts:12`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `action` | Yes | `string` |  |
| `why` | Yes | `string` |  |

## class RedeemShareDTO

- Source: `src/activity/dto/redeemShare.dto.ts:4`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `sourceId` | Yes | `string` | `@IsUUID` |
| `code` | Yes | `string` | `@IsString` |

## enum ReferralCodePrefix

- Source: `src/user/utils/referral.ts:4`

| Member | Value |
|---|---|
| `REF` | `'REF'` |
| `INVITE` | `'INV'` |

## class ReferralDTO

- Source: `src/user/dto/referral.dto.ts:5`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `userId` | Yes | `string` |  |
| `email` | Yes | `string` |  |
| `isActive` | Yes | `boolean` |  |
| `isEmailConfirmed` | Yes | `boolean` |  |
| `name` | Yes | `string` |  |
| `avatar` | Yes | `string` |  |
| `bonusPaid` | Yes | `number` |  |
| `createdAt` | Yes | `Date` |  |
| `referredBy` | Yes | `string` |  |

## class ReferralResponseDTO

- Source: `src/user/dto/referralResponse.dto.ts:3`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `referralCode` | Yes | `string` |  |

## class RegisterAgentDto

- Source: `src/agent/dto/register-agent.dto.ts:14`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `name` | Yes | `string` | `@IsNotEmpty`<br>`@IsString`<br>`@MaxLength(50)`<br>`@Matches(/^[a-zA-Z0-9\s\-_]+$/, { message: 'Name can only contain letters, numbers, spaces, hyphens, and underscores', })` |
| `email` | Yes | `string` | `@IsNotEmpty`<br>`@IsEmail`<br>`@Transform(({ value }) => value?.toLowerCase().trim())` |
| `username` | Yes | `string` | `@IsNotEmpty`<br>`@IsString`<br>`@MinLength(3)`<br>`@MaxLength(30)`<br>`@Transform(({ value }) => value?.toLowerCase().trim())`<br>`@Matches(/^[a-zA-Z0-9\-_]+$/, { message: 'Username can only contain letters, numbers, hyphens, and underscores (no spaces)', })` |
| `description` | No | `string` | `@IsOptional`<br>`@IsString`<br>`@MaxLength(500)` |
| `callback_url` | No | `string` | `@IsOptional`<br>`@IsUrl({ require_protocol: true, protocols: ['https'] })` |
| `avatar_url` | No | `string` | `@IsOptional`<br>`@IsUrl({ require_protocol: true, protocols: ['https'] })` |
| `wallet_address` | No | `string` | `@IsOptional`<br>`@IsString`<br>`@Matches(/^0x[a-fA-F0-9]{40}$/, { message: 'wallet_address must be a valid Ethereum address', })` |
| `operator_id` | No | `string` | `@IsOptional`<br>`@IsUUID` |
| `operator_email` | No | `string` | `@IsOptional`<br>`@IsEmail`<br>`@Transform(({ value }) => value?.toLowerCase().trim())` |

## class RegisterListingDTO

- Source: `src/listing/dto/registerListing.dto.ts:11`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `listingId` | No | `string` | `@IsUUID`<br>`@IsOptional` |
| `userId` | No | `string` | `@IsUUID`<br>`@IsOptional` |
| `name` | Yes | `string` | `@IsString` |
| `description` | Yes | `string` | `@IsString` |
| `isDraft` | Yes | `boolean` | `@IsBoolean` |
| `contractAddress` | No | `string` | `@IsString`<br>`@IsOptional` |
| `tags` | No | `string[]` | `@IsOptional` |
| `categoryId` | Yes | `number` | `@IsNumber` |
| `contractTypeId` | Yes | `number` | `@IsNumber` |
| `royalty` | Yes | `number` | `@IsNumber` |
| `subcategories` | No | `number[]` | `@IsArray`<br>`@IsOptional` |
| `subsubcategories` | No | `number[]` | `@IsArray`<br>`@IsOptional` |
| `attributes` | Yes | `string` | `@IsString`<br>`@IsOptional` |
| `prompt` | No | `string` | `@IsString`<br>`@IsOptional` |
| `model` | No | `string` | `@IsString`<br>`@IsOptional` |
| `isPrivate` | No | `boolean` | `@IsBoolean`<br>`@IsOptional` |

## class RegisterWebhookDTO

- Source: `src/webhook/dto/register-webhook.dto.ts:3`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `url` | Yes | `string` | `@IsUrl({ protocols: ['https'], require_protocol: true })` |
| `events` | Yes | `string[]` | `@IsArray`<br>`@ArrayMinSize(1)`<br>`@IsString({ each: true })` |

## class RegistrationToken

- Source: `src/user/entities/registrationToken.entity.ts:14`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `id` | Yes | `string` | `@PrimaryGeneratedColumn('uuid')` |
| `invitor` | Yes | `User` | `@ManyToOne(() => User, { nullable: true })`<br>`@JoinColumn([{ name: 'invitor_id', referencedColumnName: 'userId' }])` |
| `invitorId` | Yes | `string \| null` | `@Column('uuid', { name: 'invitor_id', nullable: true })` |
| `token` | Yes | `string` | `@Column('character varying', { name: 'token', length: 64, unique: true })` |
| `email` | Yes | `string \| null` | `@Column('character varying', { name: 'email', length: 255, nullable: true })` |
| `isUsed` | Yes | `boolean` | `@Column('boolean', { name: 'is_used', default: false })` |
| `expiresAt` | Yes | `Date \| null` | `@Column('timestamp', { name: 'expires_at', nullable: true })` |
| `createdAt` | Yes | `Date` | `@CreateDateColumn({ name: 'created_at' })` |

## class RejectListingDTO

- Source: `src/listing/dto/rejectListing.dto.ts:4`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `listingId` | Yes | `string` | `@IsUUID` |
| `reason` | Yes | `string` | `@IsString` |

## class RejectUserWhitelistRequestByAdminDTO

- Source: `src/activity/dto/rejectUserWhitelistRequestByAdmin.dto.ts:4`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `whitelistRequestId` | Yes | `string` | `@IsUUID` |
| `userId` | Yes | `string` | `@IsString` |
| `reason` | Yes | `string` | `@IsString` |

## class RejectUserWhitelistRequestDTO

- Source: `src/activity/dto/rejectUserWhitelistRequest.dto.ts:4`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `token` | Yes | `string` | `@IsString` |

## class RelatedAssets

- Source: `src/listing/dto/asset.dto.ts:102`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `assetId` | Yes | `string` |  |
| `type` | Yes | `string` |  |

## class RemoveBidDTO

- Source: `src/auction/dto/removeBid.dto.ts:4`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `listingId` | Yes | `string` | `@IsUUID` |
| `bidderId` | Yes | `string` | `@IsUUID` |
| `bid` | Yes | `number` | `@IsNumber` |

## class RemoveCategoryDTO

- Source: `src/listing/dto/removeCategory.dto.ts:4`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `categoryId` | Yes | `number` | `@IsNumber` |
| `hardRemove` | Yes | `boolean` | `@IsBoolean` |

## class RemoveOfferDTO

- Source: `src/marketplace/dto/removeOffer.dto.ts:4`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `listingId` | Yes | `string` | `@IsUUID` |
| `creatorId` | Yes | `string` | `@IsUUID` |

## class ReorderFolderInput

- Source: `src/folder/dto/reorder-folder.dto.ts:4`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `listingId` | Yes | `string` | `@IsUUID` |
| `afterId` | No | `string` | `@IsUUID`<br>`@IsOptional` |
| `beforeId` | No | `string` | `@IsUUID`<br>`@IsOptional` |

## class ReorderFolderPositionInput

- Source: `src/folder/dto/reorder-folder-position.dto.ts:4`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `folderId` | Yes | `string` | `@IsUUID` |
| `afterFolderId` | No | `string` | `@IsUUID`<br>`@IsOptional` |
| `beforeFolderId` | No | `string` | `@IsUUID`<br>`@IsOptional` |

## class ReorderQueueEntryInput

- Source: `src/user-feed-queue/dto/reorder-queue-entry.dto.ts:4`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `entryId` | Yes | `string` | `@IsUUID` |
| `afterEntryId` | No | `string` | `@IsOptional`<br>`@IsUUID` |
| `beforeEntryId` | No | `string` | `@IsOptional`<br>`@IsUUID` |

## class RepeatBuyerRateDTO

- Source: `src/analytics/dto/repeat-buyer-rate.dto.ts:3`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `totalBuyers` | Yes | `number` |  |
| `repeatBuyers` | Yes | `number` |  |
| `rate` | Yes | `number` |  |

## interface RetryOptions
_Max attempts (including first). Default: 3_

- Source: `src/resilience/retry/retry.types.ts:1`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `attempts` | No | `number` |  |
| `baseDelay` | No | `number` |  |
| `backoff` | No | `'exponential' \| 'fixed'` |  |
| `jitter` | No | `number` |  |
| `retryableStatuses` | No | `number[]` |  |
| `retryableErrorCodes` | No | `string[]` |  |
| `onRetry` | No | `(attempt: number, error: any) => void` |  |

## class ReviewAppealDto

- Source: `src/agent/agent-admin.controller.ts:16`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `approved` | Yes | `boolean` | `@IsBoolean`<br>`@Transform(({ value }) => value === true \|\| value === 'true')` |
| `notes` | No | `string` | `@IsOptional`<br>`@IsString` |

## class RewardTokenInforDTO

- Source: `src/user/dto/rewardTokenInfor.dto.ts:3`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `totalSupply` | Yes | `number` |  |
| `totalUnredeemed` | Yes | `number` |  |
| `totalRedeemed` | Yes | `number` |  |
| `totalReserve` | Yes | `number` |  |

## class Role

- Source: `src/user/entities/role.entity.ts:14`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `roleId` | Yes | `number` | `@PrimaryGeneratedColumn({ name: 'role_id' })` |
| `name` | Yes | `string` | `@Column('character varying', { name: 'name' })` |
| `users` | Yes | `User[]` | `@OneToMany(() => User, (users) => users.role)` |
| `createdAt` | Yes | `Date` | `@CreateDateColumn({ name: 'created_at' })` |
| `updatedAt` | Yes | `Date` | `@UpdateDateColumn({ name: 'updated_at' })` |
| `deletedAt` | Yes | `Date` | `@DeleteDateColumn({ name: 'deleted_at' })` |

## type RoleType

- Source: `src/utils/types.ts:1`
- Type: `'admin' \| 'user'`

## class RoyaltyPaidDTO

- Source: `src/marketplace/dto/royaltyPaid.dto.ts:4`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `transactionHash` | Yes | `string` | `@IsString` |
| `blockNumber` | Yes | `number` | `@IsNumber` |
| `paytokenC` | Yes | `string` | `@IsEthereumAddress` |
| `fromC` | Yes | `string` | `@IsEthereumAddress` |
| `toC` | Yes | `string` | `@IsEthereumAddress` |
| `percentage` | Yes | `string` | `@IsString` |
| `amount` | Yes | `string` | `@IsString` |

## type SanitizedDetails

- Source: `src/utils/sanitize-details.ts:29`
- Type: `Record<string, Primitive \| Primitive[]>`

## class SearchFoldersInput

- Source: `src/search/dto/search-folders.input.ts:14`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `q` | No | `string` | `@IsString`<br>`@IsOptional` |
| `limit` | No | `number` | `@IsInt`<br>`@Min(1)`<br>`@Max(100)`<br>`@IsOptional` |
| `offset` | No | `number` | `@IsInt`<br>`@Min(0)`<br>`@IsOptional` |
| `type` | No | `FolderType` | `@IsEnum(FolderType)`<br>`@IsOptional` |
| `mediaType` | No | `string` | `@IsString`<br>`@IsOptional` |
| `ownerUserName` | No | `string` | `@IsString`<br>`@IsOptional` |
| `sortBy` | No | `FolderSortBy` | `@IsEnum(FolderSortBy)`<br>`@IsOptional` |

## class SearchNamesDTO

- Source: `src/listing/dto/searchNames.dto.ts:4`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `search` | Yes | `string` | `@MinLength(2)` |

## class SearchNamesResponseDTO

- Source: `src/listing/dto/searchNamesResponse.dto.ts:5`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `listings` | Yes | `ListingDTO[]` |  |
| `users` | Yes | `PublicUser[]` |  |

## class SelfPerformanceQueryDto

- Source: `src/agent/dto/analytics-query.dto.ts:87`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `period` | No | `string` | `@IsOptional`<br>`@IsIn(['7d', '30d', '90d'])` |

## class SellingStatus

- Source: `src/listing/entities/sellingStatus.entity.ts:13`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `sellingStatusId` | Yes | `number` | `@PrimaryGeneratedColumn({ name: 'selling_status_id' })` |
| `name` | Yes | `string` | `@Column('character varying', { name: 'name' })` |
| `listings` | Yes | `Listing[]` | `@OneToMany(() => Listing, (listings) => listings.sellingStatus)` |
| `createdAt` | Yes | `Date` | `@CreateDateColumn({ name: 'created_at' })` |
| `updatedAt` | Yes | `Date` | `@UpdateDateColumn({ name: 'updated_at' })` |
| `deletedAt` | Yes | `Date` | `@DeleteDateColumn({ name: 'deleted_at' })` |

## class SendMemeTokenDTO

- Source: `src/listing/dto/sendMemeToken.dto.ts:4`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `tokenAddress` | Yes | `string` | `@IsEthereumAddress` |
| `recipientAddress` | Yes | `string` | `@IsEthereumAddress` |
| `amount` | Yes | `number` | `@IsNumber` |

## class Session

- Source: `src/user/entities/session.entity.ts:12`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `id` | Yes | `string` | `@PrimaryColumn({ type: 'text' })` |
| `token` | Yes | `string` | `@Column({ type: 'text', unique: true })` |
| `expiresAt` | Yes | `Date` | `@Column({ type: 'timestamp' })` |
| `ipAddress` | Yes | `string` | `@Column({ type: 'text', nullable: true })` |
| `userAgent` | Yes | `string` | `@Column({ type: 'text', nullable: true })` |
| `userId` | Yes | `string` | `@Column({ type: 'text' })` |
| `user` | Yes | `User` | `@ManyToOne(() => User, (user) => user.sessions)`<br>`@JoinColumn([{ name: 'userId', referencedColumnName: 'id' }])` |
| `createdAt` | Yes | `Date` | `@CreateDateColumn` |
| `updatedAt` | Yes | `Date` | `@UpdateDateColumn` |

## interface SessionEntry

- Source: `src/agent/dto/agent-session.dto.ts:1`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `id` | Yes | `string` |  |
| `ip_address` | Yes | `string \| null` |  |
| `user_agent` | Yes | `string \| null` |  |
| `created_at` | Yes | `string` |  |
| `expires_at` | Yes | `string` |  |

## interface SessionResponse

- Source: `src/agent/dto/agent-session.dto.ts:9`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `sessions` | Yes | `SessionEntry[]` |  |

## class SetAssetFlagReviewedDTO

- Source: `src/listing/dto/setAssetFlagReviewed.dto.ts:4`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `assetFlagId` | Yes | `string` | `@IsUUID` |
| `decision` | Yes | `string` | `@IsString`<br>`@IsOptional` |

## class SetDownloadPriceDTO

- Source: `src/listing/dto/setDownloadPrice.dto.ts:4`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `listingId` | Yes | `string` | `@IsString` |
| `downloadPrice` | Yes | `number` | `@IsNumber`<br>`@Min(0)` |

## class SetupPayPalDto

- Source: `src/agent/dto/setup-paypal.dto.ts:3`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `return_url` | Yes | `string` | `@IsUrl` |
| `cancel_url` | Yes | `string` | `@IsUrl` |

## class Share

- Source: `src/activity/entities/share.entity.ts:15`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `shareId` | Yes | `string` | `@PrimaryGeneratedColumn('uuid', { name: 'share_id' })` |
| `userId` | Yes | `string` | `@Column({ name: 'user_id' })` |
| `user` | Yes | `User` | `@ManyToOne(() => User, (user) => user.shares)`<br>`@JoinColumn({ name: 'user_id', referencedColumnName: 'userId' })` |
| `sourceId` | Yes | `string` | `@Column('uuid', { name: 'source_id', nullable: true })` |
| `code` | Yes | `string` | `@Column({ name: 'code', nullable: true })` |
| `paidShare` | Yes | `boolean` | `@Column({ name: 'paid_share', default: false })` |
| `createdAt` | Yes | `Date` | `@CreateDateColumn({ name: 'created_at' })` |
| `updatedAt` | Yes | `Date` | `@UpdateDateColumn({ name: 'updated_at' })` |

## class SignMessageDTO

- Source: `src/activity/dto/signMessage.dto.ts:3`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `amount` | Yes | `string` |  |
| `nonce` | Yes | `number` |  |

## type SitemapChangefreq

- Source: `src/sitemap/sitemap.types.ts:1`
- Type: `'daily' \| 'weekly' \| 'monthly' \| 'yearly'`

## class SocialMedia

- Source: `src/user/entities/socialMedia.entity.ts:15`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `socialMediaId` | Yes | `number` | `@PrimaryGeneratedColumn({ name: 'social_media_id' })` |
| `name` | Yes | `string` | `@Column('character varying', { name: 'name' })` |
| `url` | Yes | `string` | `@Column('character varying', { name: 'url' })` |
| `subscribers` | Yes | `number` | `@Column('integer')` |
| `userId` | Yes | `string` | `@Column({ name: 'user_id' })` |
| `user` | Yes | `User` | `@ManyToOne(() => User, (user) => user.socialMedia)`<br>`@JoinColumn({ name: 'user_id', referencedColumnName: 'userId' })` |
| `createdAt` | Yes | `Date` | `@CreateDateColumn({ name: 'created_at' })` |
| `updatedAt` | Yes | `Date` | `@UpdateDateColumn({ name: 'updated_at' })` |
| `deletedAt` | Yes | `Date` | `@DeleteDateColumn({ name: 'deleted_at' })` |

## class SocialMediaDTO

- Source: `src/user/dto/socialMedia.dto.ts:19`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `socialMediaList` | Yes | `SocialMediaItem[]` | `@IsArray` |

## class SocialMediaItem

- Source: `src/user/dto/socialMedia.dto.ts:4`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `platform` | Yes | `string` | `@IsString` |
| `url` | Yes | `string` | `@IsString` |
| `subscribers` | Yes | `number` | `@IsNumber` |

## class SourceMetadataType

- Source: `src/listing/dto/source-metadata.dto.ts:3`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `mediaType` | No | `string` |  |
| `duration` | No | `number` |  |
| `bitrate` | No | `number` |  |
| `codec` | No | `string` |  |
| `fps` | No | `number` |  |
| `sampleRate` | No | `number` |  |
| `contentLength` | No | `number` |  |
| `contentType` | No | `string` |  |
| `width` | No | `number` |  |
| `height` | No | `number` |  |
| `formats` | No | `string[]` |  |

## enum StaticErrors

- Source: `src/utils/customException.ts:4`

| Member | Value |
|---|---|
| `AI_MODEL_NOT_FOUND` | `'AI model not found'` |
| `AI_MODEL_REQUIRES_CATEGORY` | `'AI model must have at least one category'` |
| `MULTIPLE_ASSET_NOT_ALLOWED` | `'Multiple asset not allowed'` |
| `ASSETS_NOT_READY` | `'Your media files are not ready yet'` |
| `ASSET_INTEGRITY_FAILED` | `'One or more assets failed quality checks'` |
| `ASSET_INTEGRITY_PENDING` | `'Asset integrity check not complete — please wait'` |
| `ASSETS_ALREADY_USED` | `'Your media files are already used'` |
| `ALREADY_HAS_DOWNLOAD_LICENSE` | `'You already have a download license for this listing'` |
| `BAD_WORD_DETECTED` | `'Bad word'` |
| `BUYER_NOT_ONBOARDED` | `'You need a PayPal Business account connected to purchase ownership of listings.'` |
| `CANT_BUY_OWN_LISTING` | `'Cannot buy your own listing'` |
| `CANT_CANCEL_SUBSCRIPTION` | `'Cannot cancel subscription'` |
| `CANT_CHANGE_LISTING_STATUS` | `'Cannot change listing status'` |
| `CANT_DOWNLOAD_ASSET` | `'Cannot download Asset'` |
| `CANT_REMOVE_ITEM` | `'Cannot remove the item'` |
| `CANT_REMOVE_LISTING` | `'Cannot remove listing'` |
| `CANT_REMOVE_TOKEN` | `'Cannot remove Token'` |
| `CATEGORY_IN_USE` | `'Category is in use'` |
| `CHECK_ASSET_MODERATION` | `'Check moderation tab first'` |
| `CONFIG_NOT_FOUND` | `'Config Not Found'` |
| `DB_QUERY_FAILED` | `'DB Query failed'` |
| `DOWNLOADED_MAX` | `'User reached the download limit'` |
| `EMAIL_ALREADY_CONFIRMED` | `'Email is already confirmed'` |
| `EMAIL_ALREADY_IN_WAITLIST` | `'Email is already in waitlist'` |
| `EMAIL_NOT_CONFIRMED` | `'Email is not confirmed'` |
| `EMAIL_REGISTERED` | `'The email is already registered.'` |
| `INVITE_REGISTERED_EMAIL` | `'The email you’re trying to invite is already registered.'` |
| `EMAIL_VERIFICATION_FAILED` | `'Email verification failed'` |
| `EXCEED_MAX_PAID_SHARE` | `'Exceed max paid share per user'` |
| `EXIST_TRANSACTION` | `'The transaction exists'` |
| `FILE_SIZE_EXCEEDED` | `'File size exceeds the maximum allowed size of 100MB'` |
| `FOLLOW_REQUEST_FAILED` | `'Follow request failed'` |
| `INVALID_AMOUNT` | `'Invalid amount'` |
| `INVALID_EMAIL` | `"Email doesn't exist"` |
| `INVALID_INVITE_CODE` | `'Invalid invite code'` |
| `INVALID_FILE_EXTENSION` | `'ZIP bundle must have .zip file extension'` |
| `INVALID_THUMBNAIL_EXTENSION` | `'Thumbnail must be .jpg, .jpeg, .png, .gif, .webp, or .avif'` |
| `INVALID_PARAMETERS` | `'Invalid parameters received'` |
| `INVALID_PASSWORD` | `'Invalid password'` |
| `INVALID_REFERRAL_CODE` | `'Invalid referral code'` |
| `INVALID_SOCIAL_TOKEN` | `'Invalid Auth0 token'` |
| `INVALID_TOKEN` | `'Invalid token'` |
| `INVALID_TX_HASH` | `'Invalid Tx Hash'` |
| `INVALID_URL` | `'Invalid URL'` |
| `INVALID_USER_PASS` | `'Invalid Username and/or Password'` |
| `INVITE_LIMIT_REACHED` | `'Invite limit reached. You will be added to the waitlist'` |
| `INVITE_SAME_USER` | `'Not allow to invite to your same account.'` |
| `IPFS_NOT_SAVED` | `'Ipfs not saved'` |
| `IPFS_UPLOAD_ERROR` | `'An error occurred with IPFS'` |
| `ITEM_NOT_FOUND` | `'Item not found'` |
| `KYC_ALREADY_DONE` | `'KYC is already done'` |
| `LIKE_LISTING_FAILED` | `'Like listing failed'` |
| `MAX_DIRECT_SIGNUP_LIMIT_REACHED` | `'Max direct signup limit reached. You will be added to the waitlist'` |
| `MIN_PRICE_TWO_DOLLARS` | `'Minimum amount is $2.00'` |
| `LISTING_IS_NOT_IN_PREMINT` | `'Listing is not in PREMINT'` |
| `LISTING_MINT_NOT_ALLOWED` | `'Minting is not allowed'` |
| `LISTING_NOT_FOR_SALE` | `'Listing is not for sale'` |
| `LISTING_NOT_FOUND` | `'Listing not found'` |
| `NON_EXIST_FILE` | `'The file does not exist'` |
| `NOT_LISTING_OWNER` | `'User does not own the listing'` |
| `NOT_OWNER` | `'Not Owner'` |
| `NO_ACTIVE_SUBSCRIPTION` | `'No active subscription found'` |
| `NO_BILLING_ACCOUNT` | `'No billing account found'` |
| `NO_CHANGES_DETECTED` | `'No changes was detected'` |
| `OFFER_EXISTS` | `'Offer exists'` |
| `OFFER_NOT_FOUND` | `'Offer not found'` |
| `OFFER_PROCESSING` | `'Offer is being processed'` |
| `INVALID_OFFER_STATUS` | `'Offer status does not allow this action'` |
| `OFFER_COUNTER_LIMIT_REACHED` | `'Maximum counter-offer rounds reached'` |
| `OFFER_EXPIRED` | `'Offer has expired'` |
| `PAID_SHARE_NOT_RESET` | `'Paid share is not reset yet'` |
| `PARENT_HAS_NO_PARENT` | `'The selected parent must not have a parent itself'` |
| `PARENT_NOT_TOP_LEVEL` | `'parent_id must reference a top-level comment — nested threads are not supported'` |
| `PASSWORD_RESET_LINK_EXPIRED` | `'Password reset link is expired'` |
| `PAYMENT_REQUIRED` | `'Payment required'` |
| `PAYPAL_NOT_FOUND` | `'No PayPal account found for your email'` |
| `PAYPAY_AUTH_EXPIRED` | `'PayPal Authorization Expired'` |
| `REPLY_TO_CROSS_THREAD` | `'reply_to must reference the parent comment or a reply in the same thread'` |
| `REPLY_TO_REQUIRES_PARENT` | `'reply_to requires parent_id — set parent_id to the top-level comment of the thread'` |
| `REWARD_TYPE_ALREADY_EXISTS` | `'A reward type with this name already exists'` |
| `REWARD_TYPE_NOT_FOUND` | `'Reward Type Not Found'` |
| `S3_ERROR` | `'An error occurred with Amazon S3'` |
| `SELLER_NOT_REGISTERED` | `'Please set up your PayPal account to accept offers.'` |
| `SELLER_NOT_REGISTERED_CUSTOM` | `'### is not registered to accept offers. We have sent your offer along with a message inviting them to get on board.'` |
| `SENDER_REJECTED` | `'Sender rejected'` |
| `SESSION_NOT_FOUND` | `'Session not found'` |
| `SHARE_NOT_FOUND` | `'Share not found'` |
| `SOCIAL_LOGIN_FAILED` | `'Auth0 login failed'` |
| `SUBSCRIPTION_ALREADY_ACTIVE` | `'An active subscription already exists'` |
| `SUMSUB_API_ERROR` | `"Couldn't reach SumSub API"` |
| `TOKEN_EXISTS` | `'Token exists'` |
| `TOKEN_NOT_FOUND` | `'Token not found'` |
| `TOO_MANY_REQUESTS` | `'Too many requests, please try again later'` |
| `UNAUTHORIZED` | `'Unauthorized'` |
| `UNSUPPORTED_FILE` | `'The file type is not supported'` |
| `USER_2FA_ALREADY_CONFIRMED` | `'2FA is already confirmed'` |
| `USER_2FA_REQUIRED` | `'Two-factor authentication must be enabled before admin login'` |
| `USER_NOT_FOUND` | `'User not found'` |
| `USER_SHOULD_PREMINT` | `'User needs to premint'` |
| `WALLET_ALREADY_TAKEN` | `'This wallet is already used by another user'` |
| `WALLET_IS_REQUIRED` | `'Wallet is required'` |
| `WALLET_NOT_FOUND` | `'Wallet not found'` |
| `WEB3_ISSUE` | `'Web3 Issue'` |
| `WHITELIST_REQUEST_EXISTS` | `'Whitelist request already exists'` |
| `WRONG_2FA_CODE` | `'Wrong 2FA code'` |
| `WRONG_ASSET_NAME` | `'Listing name contains disallowed characters'` |
| `WRONG_LISTING_STATUS` | `'Wrong listing status'` |
| `WRONG_PASSWORD` | `'Password is incorrect'` |
| `PAYPAL_BILLING_SETUP_FAILED` | `'PayPal billing agreement setup failed'` |
| `PAYPAL_PAYMENT_TOKEN_FAILED` | `'PayPal payment token creation failed'` |
| `PAYPAL_PAYMENT_FAILED` | `'PayPal payment failed'` |
| `SELLER_PAYMENT_NOT_READY` | `'Seller has not completed payment setup'` |
| `WRONG_PAYMENT_METHOD` | `'Wrong payment method'` |
| `WRONG_USER_NAME` | `'Username must be 1-20 characters. Only letters, numbers, hyphens, and underscores are allowed.'` |
| `USER_NAME_ALREADY_SET` | `'Username has already been set and cannot be changed.'` |
| `USER_NAME_TAKEN` | `'Username is already taken'` |
| `WRONG_BIO_LENGTH` | `'Bio must be at most 175 characters'` |
| `LISTING_NAME_TAKEN` | `'A listing with this name already exists'` |
| `WRONG_USER_NAME_LENGTH` | `'Title must be at most 50 characters'` |
| `REGISTRATION_TOKEN_EXPIRED` | `'Registration token expired'` |
| `PRICE_TOO_LOW_FOR_FEES` | `'Price is too low to cover platform and payment fees'` |
| `FOLDER_CAP_REACHED` | `'Folder cap reached for your plan'` |
| `LISTING_TERMINAL_STATE` | `'Listing is in a terminal state — no edits possible'` |
| `LISTING_EDIT_WINDOW_EXPIRED` | `'Listing edit window has expired — only some fields remain editable'` |
| `PUBLISHED_IMMUTABLE` | `'Published listings are permanent and cannot be deleted'` |
| `OPERATOR_MANAGED_BILLING` | `'Billing is managed by your operator'` |
| `CANNOT_FOLLOW_SELF` | `'You cannot follow yourself'` |
| `FOLLOW_TARGET_NOT_FOUND` | `'The user you are trying to follow does not exist'` |
| `REVIEW_ACK_REQUIRED` | `'Account is under review — resend with acknowledge_review: true to proceed'` |

## interface StaticSitemapEntry

- Source: `src/sitemap/sitemap.types.ts:3`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `url` | Yes | `string` |  |
| `changefreq` | Yes | `SitemapChangefreq` |  |
| `priority` | Yes | `number` |  |

## class SubscriptionDTO

- Source: `src/billing/dto/billing.dto.ts:8`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `plan` | Yes | `string` |  |
| `status` | Yes | `string` |  |
| `creditsBalance` | Yes | `number` |  |
| `creditsMonthlyLimit` | Yes | `number` |  |
| `currentPeriodEnd` | No | `Date` |  |
| `topUpTier` | No | `string` |  |
| `topUpActive` | Yes | `boolean` |  |
| `agentSlots` | Yes | `number` |  |
| `agentSlotsUsed` | Yes | `number` |  |
| `hasActiveApiKey` | Yes | `boolean` |  |
| `createdAt` | No | `Date` |  |
| `billingInterval` | No | `string` |  |
| `pendingDowngrade` | No | `string` |  |
| `maxPortfolios` | Yes | `number` |  |
| `maxCollections` | Yes | `number` |  |

## interface SuggestionContext

- Source: `src/agent/services/agent-home.service.ts:397`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `newFollowerCount` | Yes | `number` |  |
| `followedCreatorsPostedCount` | Yes | `number` |  |
| `daysSinceLastUpload` | Yes | `number \| null` |  |

## class Tag

- Source: `src/listing/entities/tag.entity.ts:13`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `tagId` | Yes | `number` | `@PrimaryGeneratedColumn({ name: 'tag_id' })` |
| `name` | Yes | `string` | `@Column('character varying', { name: 'name' })` |
| `listingToTags` | Yes | `ListingToTag[]` | `@OneToMany(() => ListingToTag, (listingToTags) => listingToTags.tag)` |
| `createdAt` | Yes | `Date` | `@CreateDateColumn({ name: 'created_at' })` |
| `updatedAt` | Yes | `Date` | `@UpdateDateColumn({ name: 'updated_at' })` |
| `deletedAt` | Yes | `Date` | `@DeleteDateColumn({ name: 'deleted_at' })` |

## class TelegramLink

- Source: `src/notifications/entities/telegram-link.entity.ts:13`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `id` | Yes | `string` | `@PrimaryGeneratedColumn('uuid', { name: 'id' })` |
| `userId` | Yes | `string` | `@Column('uuid', { name: 'user_id', unique: true })` |
| `user` | Yes | `User` | `@ManyToOne(() => User)`<br>`@JoinColumn({ name: 'user_id', referencedColumnName: 'userId' })` |
| `chatId` | Yes | `string` | `@Column('bigint', { name: 'chat_id' })` |
| `username` | Yes | `string` | `@Column('varchar', { length: 100, nullable: true })` |
| `active` | Yes | `boolean` | `@Column('boolean', { default: true })` |
| `linkedAt` | Yes | `Date` | `@Column({ name: 'linked_at', type: 'timestamptz', default: () => 'NOW()' })` |
| `createdAt` | Yes | `Date` | `@CreateDateColumn({ name: 'created_at' })` |
| `updatedAt` | Yes | `Date` | `@UpdateDateColumn({ name: 'updated_at' })` |

## interface TelegramPayload

- Source: `src/notifications/types/payloads.ts:18`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `text` | Yes | `string` |  |
| `parseMode` | No | `'HTML' \| 'MarkdownV2'` |  |

## class TierConfigDTO

- Source: `src/permissions/dto/fetchAllTiers.dto.ts:54`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `free` | Yes | `TierPermissionsDTO` |  |
| `pro` | Yes | `TierPermissionsDTO` |  |
| `founders` | Yes | `TierPermissionsDTO` |  |

## class TierPermissionsDTO

- Source: `src/permissions/dto/fetchAllTiers.dto.ts:3`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `show_verified_badge` | Yes | `boolean` |  |
| `custom_avatar_border` | Yes | `boolean` |  |
| `profile_title` | Yes | `boolean` |  |
| `show_rewards` | Yes | `boolean` |  |
| `download_assets` | Yes | `string \| boolean` |  |
| `make_offers` | Yes | `boolean` |  |
| `filter_offers` | Yes | `string \| boolean` |  |
| `view_tx_history` | Yes | `boolean` |  |
| `view_viral_score` | Yes | `boolean` |  |
| `access_ai_tools` | Yes | `string \| boolean` |  |
| `report_asset` | Yes | `boolean` |  |
| `view_prompts` | Yes | `string \| boolean` |  |
| `max_invites` | Yes | `number` |  |
| `hide_ads` | Yes | `boolean` |  |
| `show_avatar_on_listings` | Yes | `boolean` |  |
| `make_private` | Yes | `boolean` |  |

## class TierPriceDTO

- Source: `src/billing/dto/billing.dto.ts:185`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `plan` | Yes | `string` |  |
| `interval` | Yes | `string` |  |
| `unitAmount` | Yes | `number` |  |
| `currency` | Yes | `string` |  |

## class ToggleFollowResponse

- Source: `src/agent/dto/social-engagement.dto.ts:77`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `followed` | Yes | `boolean` |  |

## enum TokenStatus

- Source: `src/listing/utils/listingStatus.ts:46`

| Member | Value |
|---|---|
| `SUBMITTED` | `'submitted'` |
| `PENDING` | `'pending'` |
| `PAID` | `'paid'` |

## enum TopUpTier

- Source: `src/billing/entities/credit-top-up.entity.ts:9`

| Member | Value |
|---|---|
| `STARTER` | `'starter'` |
| `BASIC` | `'basic'` |
| `PLUS` | `'plus'` |
| `POWER` | `'power'` |

## class TopUpTierDTO

- Source: `src/billing/dto/billing.dto.ts:146`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `tier` | Yes | `string` |  |
| `priceCents` | Yes | `number` |  |
| `triggerThreshold` | Yes | `number` |  |
| `creditsPerCharge` | Yes | `number` |  |

## class TradeHistory

- Source: `src/activity/entities/tradeHistory.entity.ts:19`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `tradeHistoryId` | Yes | `string` | `@PrimaryGeneratedColumn('uuid', { name: 'trade_history_id' })` |
| `sellerId` | Yes | `string` | `@Column({ name: 'seller_id' })` |
| `seller` | Yes | `User` | `@ManyToOne(() => User, (seller) => seller.sellTrades)`<br>`@JoinColumn([{ name: 'seller_id', referencedColumnName: 'userId' }])` |
| `buyerId` | Yes | `string` | `@Column({ name: 'buyer_id', nullable: true })` |
| `buyer` | Yes | `User` | `@ManyToOne(() => User, (buyer) => buyer.buyTrades)`<br>`@JoinColumn([{ name: 'buyer_id', referencedColumnName: 'userId' }])` |
| `listingId` | Yes | `string` | `@Column({ name: 'listing_id' })` |
| `listing` | Yes | `Listing` | `@ManyToOne(() => Listing, (listing) => listing.tradeHistories)`<br>`@JoinColumn({ name: 'listing_id', referencedColumnName: 'listingId' })` |
| `price` | Yes | `number` | `@Column('float', { nullable: true })` |
| `priceUsd` | Yes | `number` | `@Column({ type: 'float', name: 'price_usd', nullable: true })` |
| `saleDate` | Yes | `Date` | `@Column({ name: 'sale_date', nullable: true, type: 'timestamptz' })` |
| `isAuction` | Yes | `boolean` | `@Column({ name: 'is_auction', default: false, })` |
| `txHash` | Yes | `string` | `@Column('character varying', { name: 'tx_hash' })` |
| `paymentToken` | Yes | `string` | `@Column('character varying', { name: 'payment_token', nullable: true })` |
| `transactionId` | Yes | `string` | `@Column('uuid', { name: 'transaction_id', nullable: true })` |
| `purchaseType` | Yes | `PurchaseType` | `@Column({ type: 'enum', enum: PurchaseType, name: 'purchase_type', default: PurchaseType.OWNERSHIP, })` |
| `createdAt` | Yes | `Date` | `@CreateDateColumn({ name: 'created_at' })` |
| `updatedAt` | Yes | `Date` | `@UpdateDateColumn({ name: 'updated_at' })` |
| `deletedAt` | Yes | `Date` | `@DeleteDateColumn({ name: 'deleted_at' })` |

## class TradeHistoryDTO

- Source: `src/activity/dto/tradeHistory.dto.ts:6`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `tradeHistoryId` | Yes | `string` |  |
| `sellerId` | Yes | `string` |  |
| `seller` | Yes | `PublicUser` |  |
| `buyerId` | Yes | `string` |  |
| `buyer` | Yes | `PublicUser` |  |
| `listingId` | Yes | `string` |  |
| `listing` | Yes | `ListingDTO` |  |
| `price` | Yes | `number` |  |
| `priceUsd` | Yes | `number` |  |
| `saleDate` | Yes | `Date` |  |
| `isAuction` | Yes | `boolean` |  |
| `txHash` | Yes | `string` |  |
| `paymentToken` | Yes | `string` |  |

## class TradeHistoryQueryDto

- Source: `src/agent/dto/account.dto.ts:76`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `page` | No | `number` | `@IsOptional`<br>`@Type(() => Number)`<br>`@IsInt`<br>`@Min(1)` |
| `limit` | No | `number` | `@IsOptional`<br>`@Type(() => Number)`<br>`@IsInt`<br>`@Min(1)`<br>`@Max(100)` |

## class Transaction

- Source: `src/listing/entities/transaction.entity.ts:16`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `transactionId` | Yes | `string` | `@PrimaryGeneratedColumn('uuid', { name: 'transaction_id' })` |
| `orderId` | Yes | `string \| null` | `@Column('character varying', { name: 'order_id', nullable: true })` |
| `status` | Yes | `TransactionStatusType` | `@Column({ type: 'enum', enum: TransactionStatusType })` |
| `reason` | Yes | `string` | `@Column('character varying', { name: 'reason', nullable: true })` |
| `amount` | Yes | `string` | `@Column('character varying', { name: 'amount' })` |
| `amountInUSD` | Yes | `string` | `@Column('character varying', { name: 'amount_in_usd' })` |
| `currency` | Yes | `string` | `@Column('character varying', { name: 'currency' })` |
| `transactionHash` | Yes | `string` | `@Column('character varying', { name: 'transaction_hash', nullable: true })` |
| `listingId` | Yes | `string` | `@Column({ name: 'listing_id' })` |
| `listing` | Yes | `Listing` | `@ManyToOne(() => Listing, (listing) => listing.transactions)`<br>`@JoinColumn({ name: 'listing_id', referencedColumnName: 'listingId' })` |
| `userId` | Yes | `string` | `@Column({ name: 'user_id' })` |
| `user` | Yes | `User` | `@ManyToOne(() => User, (user) => user.transactions)`<br>`@JoinColumn({ name: 'user_id', referencedColumnName: 'userId' })` |
| `purchaseType` | Yes | `PurchaseType` | `@Column({ type: 'enum', enum: PurchaseType, name: 'purchase_type', default: PurchaseType.OWNERSHIP, })` |
| `createdAt` | Yes | `Date` | `@CreateDateColumn({ name: 'created_at' })` |

## class TransactionDTO

- Source: `src/listing/dto/transaction.dto.ts:4`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `listingId` | Yes | `string` | `@IsString` |
| `orderId` | Yes | `string` | `@IsString` |
| `amount` | Yes | `string` | `@IsString` |
| `amountInUSD` | Yes | `string` | `@IsString` |
| `currency` | Yes | `string` | `@IsString` |

## class TransactionHashDTO

- Source: `src/listing/dto/transactionHash.dto.ts:4`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `listingId` | Yes | `string` | `@IsString` |
| `txHash` | Yes | `string` | `@IsString` |
| `listingStatusId` | Yes | `number` | `@IsNumber` |

## class TransactionHistoryDTO

- Source: `src/analytics/dto/transaction-history.dto.ts:30`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `items` | Yes | `TransactionHistoryItemDTO[]` |  |
| `nextCursor` | No | `string` |  |
| `hasMore` | Yes | `boolean` |  |

## class TransactionHistoryItemDTO

- Source: `src/analytics/dto/transaction-history.dto.ts:3`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `id` | Yes | `string` |  |
| `buyerId` | Yes | `string` |  |
| `buyerName` | No | `string` |  |
| `sellerId` | Yes | `string` |  |
| `sellerName` | No | `string` |  |
| `price` | Yes | `number` |  |
| `date` | Yes | `Date` |  |
| `isAuction` | Yes | `boolean` |  |

## enum TransactionStatusType

- Source: `src/utils/types.ts:59`

| Member | Value |
|---|---|
| `PENDING` | `'pending'` |
| `COMPLETED` | `'completed'` |
| `FAILED` | `'failed'` |

## class TransferListingDTO

- Source: `src/listing/dto/transferListing.dto.ts:4`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `fromC` | Yes | `string` | `@IsEthereumAddress` |
| `toC` | Yes | `string` | `@IsEthereumAddress` |
| `transactionHash` | Yes | `string` | `@IsString` |
| `tokenId` | Yes | `number` | `@IsNumber` |

## class TrendingArtistDTO

- Source: `src/viral-score/dto/trendingArtist.dto.ts:3`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `artistId` | Yes | `string` |  |
| `score` | Yes | `number` |  |

## interface TrendingItem

- Source: `src/agent/services/agent-home.service.ts:389`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `listing_id` | Yes | `string` |  |
| `name` | Yes | `string` |  |
| `creator` | Yes | `string` |  |
| `viral_score` | Yes | `number` |  |
| `like_count` | Yes | `number` |  |

## class TrendingListingDTO

- Source: `src/analytics/dto/trending.dto.ts:3`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `listingId` | Yes | `string` |  |
| `name` | No | `string` |  |
| `velocityScore` | Yes | `number` |  |
| `views` | Yes | `number` |  |
| `sales` | No | `number` |  |
| `priceChange` | No | `number` |  |

## class TrendingListingDTO

- Source: `src/viral-score/dto/trendingListing.dto.ts:3`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `listing` | Yes | `ListingDTO` |  |
| `score` | Yes | `number` |  |

## class TrendingListingsDTO

- Source: `src/analytics/dto/trending.dto.ts:24`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `listings` | Yes | `TrendingListingDTO[]` |  |
| `period` | Yes | `string` |  |

## class TrendingQueryDto

- Source: `src/agent/dto/analytics-query.dto.ts:38`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `period` | No | `string` | `@IsOptional`<br>`@IsIn(['1h', '6h', '24h', '7d'])` |
| `limit` | No | `number` | `@IsOptional`<br>`@Type(() => Number)`<br>`@IsInt`<br>`@Min(1)`<br>`@Max(50)` |

## class TwoFaDisableDto

- Source: `src/agent/dto/2fa-disable.dto.ts:4`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `code` | Yes | `string` | `@IsString`<br>`@Length(6, 6)` |
| `password` | Yes | `string` | `@IsString`<br>`@MinLength(PASSWORD_RULES.minLength)`<br>`@MaxLength(PASSWORD_RULES.maxLength)` |

## class TwoFaEnableDto

- Source: `src/agent/dto/2fa-enable.dto.ts:4`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `password` | Yes | `string` | `@IsString`<br>`@MinLength(PASSWORD_RULES.minLength)`<br>`@MaxLength(PASSWORD_RULES.maxLength)` |

## interface TypesenseFolderDoc

- Source: `src/search/dto/typesense-folder.dto.ts:7`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `id` | Yes | `string` |  |
| `sortKey` | Yes | `number` |  |
| `name` | Yes | `string` |  |
| `description` | No | `string` |  |
| `tags` | No | `string[]` |  |
| `type` | Yes | `string` |  |
| `ownerId` | Yes | `string` |  |
| `ownerUserName` | Yes | `string` |  |
| `ownerName` | No | `string` |  |
| `thumbnailUrl` | No | `string` |  |
| `effectiveThumbnailUrl` | No | `string` |  |
| `url` | Yes | `string` |  |
| `createdAt` | Yes | `number` |  |
| `updatedAt` | Yes | `number` |  |
| `childLastUpdatedAt` | No | `number` |  |
| `likeCount` | Yes | `number` |  |
| `saveCount` | Yes | `number` |  |
| `followCount` | Yes | `number` |  |
| `viralScore` | Yes | `number` |  |
| `listingCount` | Yes | `number` |  |
| `totalLikes` | Yes | `number` |  |
| `totalViews` | Yes | `number` |  |
| `mediaTypes` | No | `string[]` |  |
| `priceMin` | No | `number` |  |
| `priceMax` | No | `number` |  |

## interface TypesenseListingDoc

- Source: `src/search/dto/typesense-listing.dto.ts:5`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `id` | Yes | `string` |  |
| `sortKey` | Yes | `number` |  |
| `name` | Yes | `string` |  |
| `slug` | Yes | `string` |  |
| `description` | Yes | `string` |  |
| `prompt` | Yes | `string` |  |
| `tags` | Yes | `string[]` |  |
| `categoryName` | Yes | `string` |  |
| `subcategoryNames` | Yes | `string[]` |  |
| `creatorName` | Yes | `string` |  |
| `creatorUserName` | Yes | `string` |  |
| `creatorId` | Yes | `string` |  |
| `ownerId` | Yes | `string` |  |
| `mediaType` | Yes | `string` |  |
| `price` | Yes | `number` |  |
| `paymentMethod` | Yes | `string` |  |
| `contractTypeName` | Yes | `string` |  |
| `statusId` | Yes | `number` |  |
| `isListed` | Yes | `boolean` |  |
| `listedAt` | Yes | `number` |  |
| `createdAt` | Yes | `number` |  |
| `viralScore` | Yes | `number` |  |
| `viewCount` | Yes | `number` |  |
| `likeCount` | Yes | `number` |  |
| `purchaseCount` | Yes | `number` |  |
| `ownershipSalesCount` | Yes | `number` |  |
| `downloadSalesCount` | Yes | `number` |  |
| `ownershipRevenue` | Yes | `number` |  |
| `downloadRevenue` | Yes | `number` |  |
| `salesCount` | Yes | `number` |  |
| `totalRevenue` | Yes | `number` |  |
| `saleEndsAt` | Yes | `number` |  |
| `hasActiveOffers` | Yes | `boolean` |  |
| `hasActiveBids` | Yes | `boolean` |  |
| `isPrivate` | Yes | `boolean` |  |
| `private_portfolio` | Yes | `boolean` |  |
| `allowCommercialUse` | No | `boolean` |  |
| `duration` | No | `number` |  |

## interface TypesenseUserDoc

- Source: `src/search/dto/typesense-user.dto.ts:4`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `id` | Yes | `string` |  |
| `name` | Yes | `string` |  |
| `userName` | Yes | `string` |  |
| `avatar` | Yes | `string` |  |
| `bio` | Yes | `string` |  |
| `isAgent` | Yes | `boolean` |  |
| `planCode` | Yes | `string` |  |
| `createdAt` | Yes | `number` |  |
| `viralScore` | Yes | `number` |  |
| `followerCount` | Yes | `number` |  |
| `followingCount` | Yes | `number` |  |
| `listingCount` | Yes | `number` |  |

## class UpdateAgentListingDto

- Source: `src/agent/dto/create-listing.dto.ts:95`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `description` | No | `string` | `@IsOptional`<br>`@IsString`<br>`@MaxLength(5000)` |
| `tags` | No | `string[]` | `@IsOptional`<br>`@IsArray`<br>`@IsString({ each: true })`<br>`@ArrayMaxSize(20)` |
| `category_id` | No | `number` | `@IsOptional`<br>`@IsNumber`<br>`@Type(() => Number)` |
| `price` | No | `number` | `@IsOptional`<br>`@IsNumber`<br>`@Min(0)`<br>`@Type(() => Number)` |
| `private` | No | `boolean` | `@IsOptional`<br>`@IsBoolean` |
| `free_download` | No | `boolean` | `@IsOptional`<br>`@IsBoolean` |

## class UpdateAgentProfileDto

- Source: `src/agent/dto/register-agent.dto.ts:70`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `name` | No | `string` | `@IsOptional`<br>`@IsString`<br>`@MaxLength(50)`<br>`@Matches(/^[a-zA-Z0-9\s\-_]+$/, { message: 'Name can only contain letters, numbers, spaces, hyphens, and underscores', })` |
| `username` | No | `string` | `@IsOptional`<br>`@IsString`<br>`@MinLength(3)`<br>`@MaxLength(30)`<br>`@Transform(({ value }) => value?.toLowerCase().trim())`<br>`@Matches(/^[a-zA-Z0-9\-_]+$/, { message: 'Username can only contain letters, numbers, hyphens, and underscores (no spaces)', })` |
| `description` | No | `string` | `@IsOptional`<br>`@IsString`<br>`@MaxLength(500)` |
| `avatar_url` | No | `string` | `@IsOptional`<br>`@IsUrl({ require_protocol: true, protocols: ['https'] })` |
| `banner_url` | No | `string` | `@IsOptional`<br>`@IsUrl({ require_protocol: true, protocols: ['https'] })` |

## class UpdateAgentWalletDto

- Source: `src/agent/dto/register-agent.dto.ts:105`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `wallet_address` | Yes | `string` | `@IsNotEmpty`<br>`@IsString`<br>`@Matches(/^0x[a-fA-F0-9]{40}$/, { message: 'wallet_address must be a valid Ethereum address', })` |

## class UpdateAiModelDTO

- Source: `src/ai-model/dto/updateAiModel.dto.ts:3`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `aiModelId` | Yes | `number` |  |
| `name` | No | `string` |  |
| `sortOrder` | No | `number` |  |
| `isDisabled` | No | `boolean` |  |
| `categoryIds` | No | `number[]` |  |

## class UpdateFolderInput

- Source: `src/folder/dto/update-folder.dto.ts:13`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `name` | No | `string` | `@IsString`<br>`@MaxLength(100)`<br>`@IsOptional` |
| `visibility` | No | `FolderVisibility` | `@IsEnum(FolderVisibility)`<br>`@IsOptional` |
| `thumbnailUrl` | No | `string` | `@IsString`<br>`@MaxLength(2048)`<br>`@IsOptional` |
| `type` | No | `FolderType` | `@IsEnum(FolderType)`<br>`@IsIn([FolderType.COLLECTION, FolderType.PLAYLIST])`<br>`@IsOptional` |
| `description` | No | `string` | `@IsString`<br>`@MaxLength(1000)`<br>`@IsOptional` |
| `tags` | No | `string[]` | `@IsArray`<br>`@ArrayMaxSize(20)`<br>`@IsString({ each: true })`<br>`@MaxLength(32, { each: true })`<br>`@IsOptional` |

## class UpdateNotificationSettingChannelDTO

- Source: `src/notifications/dto/updateNotificationSettingChannel.dto.ts:5`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `notificationTypeId` | Yes | `number` |  |
| `channel` | Yes | `string` | `@IsIn(Object.values(NotificationChannel))` |
| `enabled` | Yes | `boolean` |  |

## class UpdatePayTokenDTO

- Source: `src/listing/dto/updatePayToken.dto.ts:4`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `payTokenAddress` | Yes | `string` | `@IsEthereumAddress` |
| `txHash` | Yes | `string` | `@IsString` |

## class UpdatePriceDto

- Source: `src/agent/dto/marketplace-purchase.dto.ts:73`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `price` | No | `number` | `@IsOptional`<br>`@IsNumber({ maxDecimalPlaces: 2 })`<br>`@Min(0)`<br>`@Type(() => Number)` |
| `download_price` | No | `number` | `@IsOptional`<br>`@IsNumber({ maxDecimalPlaces: 2 })`<br>`@Min(0.5)`<br>`@Type(() => Number)` |
| `free_download` | No | `boolean` | `@IsOptional`<br>`@IsBoolean`<br>`@Type(() => Boolean)` |

## class UpdateWebhookDTO

- Source: `src/webhook/dto/update-webhook.dto.ts:9`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `url` | No | `string` | `@IsOptional`<br>`@IsUrl({ protocols: ['https'], require_protocol: true })` |
| `events` | No | `string[]` | `@IsOptional`<br>`@IsArray`<br>`@IsString({ each: true })` |
| `active` | No | `boolean` | `@IsOptional`<br>`@IsBoolean` |

## class User
_Better Auth's TEXT PK. Kept in sync with user_id via DB trigger (see better-auth-tables.sql)._

- Source: `src/user/entities/user.entity.ts:47`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `userId` | Yes | `string` | `@PrimaryGeneratedColumn('uuid', { name: 'user_id' })` |
| `id` | Yes | `string` | `@Column('text', { name: 'id', nullable: true, unique: true })` |
| `email` | Yes | `string` | `@Column('character varying', { name: 'email', nullable: true })` |
| `password` | Yes | `string` | `@Column('character varying', { name: 'password', nullable: true })` |
| `isActive` | Yes | `boolean` | `@Column({ name: 'is_active', default: true, })` |
| `unredeemedPoint` | Yes | `number` | `@Column({ type: 'float', name: 'unredeemed_point', default: 0, })` |
| `redeemedPoint` | Yes | `number` | `@Column({ type: 'float', name: 'redeemed_point', default: 0, })` |
| `isEmailConfirmed` | Yes | `boolean` | `@Column({ name: 'is_email_confirmed', default: false, })` |
| `name` | Yes | `string` | `@Column('character varying', { name: 'name', nullable: true })` |
| `userName` | Yes | `string` | `@Column('character varying', { name: 'user_name', nullable: true })` |
| `bio` | Yes | `string` | `@Column('character varying', { name: 'bio', nullable: true })` |
| `avatar` | Yes | `string` | `@Column('character varying', { name: 'avatar', nullable: true })` |
| `banner` | Yes | `string` | `@Column('character varying', { name: 'banner', nullable: true })` |
| `twitter` | Yes | `string` | `@Column('character varying', { name: 'twitter', nullable: true })` |
| `instagram` | Yes | `string` | `@Column('character varying', { name: 'instagram', nullable: true })` |
| `website` | Yes | `string` | `@Column('character varying', { name: 'website', nullable: true })` |
| `negativePoints` | Yes | `number` | `@Column({ name: 'negative_points', nullable: true, })` |
| `walletAddress` | Yes | `string` | `@Column('character varying', { name: 'wallet_address', nullable: true, unique: true, })` |
| `twoFactorEnabled` | Yes | `boolean` | `@Column({ name: 'twoFactorEnabled', default: false, })` |
| `referralCode` | Yes | `string` | `@Column('character varying', { name: 'referral_code', nullable: true })` |
| `customInviteQuota` | Yes | `number` | `@Column({ name: 'custom_invite_quota', nullable: true, })` |
| `referrerId` | Yes | `string` | `@Column('character varying', { name: 'referrer_id', nullable: true })` |
| `referrer` | Yes | `User` | `@ManyToOne(() => User, (user) => user.referrals)`<br>`@JoinColumn([{ name: 'referrer_id', referencedColumnName: 'userId' }])` |
| `referrals` | Yes | `User[]` | `@OneToMany(() => User, (user) => user.referrer)` |
| `roleId` | Yes | `number` | `@Column('integer', { name: 'role_id' })` |
| `role` | Yes | `Role` | `@ManyToOne(() => Role, (role) => role.users)`<br>`@JoinColumn([{ name: 'role_id', referencedColumnName: 'roleId' }])` |
| `userStatusId` | Yes | `number` | `@Column('integer', { name: 'user_status_id' })` |
| `userStatus` | Yes | `UserStatus` | `@ManyToOne(() => UserStatus, (userStatus) => userStatus.users)`<br>`@JoinColumn([ { name: 'user_status_id', referencedColumnName: 'userStatusId' }, ])` |
| `creatorStatusId` | Yes | `number` | `@Column('integer', { name: 'creator_status_id', nullable: true })` |
| `creatorStatus` | Yes | `CreatorStatus` | `@ManyToOne(() => CreatorStatus, (creatorStatus) => creatorStatus.users)`<br>`@JoinColumn([ { name: 'creator_status_id', referencedColumnName: 'creatorStatusId' }, ])` |
| `paypalTrackingId` | Yes | `string` | `@Column('character varying', { name: 'paypal_tracking_id', nullable: true, })` |
| `paypalMerchantId` | Yes | `string` | `@Column('character varying', { name: 'paypal_merchant_id', nullable: true, })` |
| `isPayPalKYCed` | Yes | `boolean` | `@Column('boolean', { name: 'is_paypal_kyced', default: false })` |
| `isPayPalConsentGranted` | Yes | `boolean` | `@Column('boolean', { name: 'is_paypal_consent_granted', default: false })` |
| `userWallets` | Yes | `UserWallet[]` | `@OneToMany(() => UserWallet, (userWallet) => userWallet.user)` |
| `notificationSettings` | Yes | `NotificationSetting[]` | `@OneToMany(() => NotificationSetting, (notifications) => notifications.user)` |
| `from` | Yes | `Follow[]` | `@OneToMany(() => Follow, (from) => from.follower)` |
| `followings` | Yes | `Follow[]` | `@OneToMany(() => Follow, (followings) => followings.following)` |
| `buyTrades` | Yes | `TradeHistory[]` | `@OneToMany(() => TradeHistory, (buyTrades) => buyTrades.buyer)` |
| `sellTrades` | Yes | `TradeHistory[]` | `@OneToMany(() => TradeHistory, (sellTrades) => sellTrades.seller)` |
| `pointEarned` | Yes | `PointEarned[]` | `@OneToMany(() => PointEarned, (pointEarned) => pointEarned.user)` |
| `pointRedeemed` | Yes | `PointRedeemed[]` | `@OneToMany(() => PointRedeemed, (pointRedeemed) => pointRedeemed.user)` |
| `sessions` | Yes | `Session[]` | `@OneToMany(() => Session, (sessions) => sessions.user)` |
| `createdListings` | Yes | `Listing[]` | `@OneToMany(() => Listing, (listings) => listings.artist)` |
| `listings` | Yes | `Listing[]` | `@OneToMany(() => Listing, (listings) => listings.user)` |
| `likes` | Yes | `Like[]` | `@OneToMany(() => Like, (likes) => likes.user)` |
| `views` | Yes | `View[]` | `@OneToMany(() => View, (views) => views.user)` |
| `eventLedgerEntries` | Yes | `EventLedger[]` | `@OneToMany(() => EventLedger, (el) => el.user)` |
| `bids` | Yes | `Bid[]` | `@OneToMany(() => Bid, (bids) => bids.bidder)` |
| `offers` | Yes | `Offer[]` | `@OneToMany(() => Offer, (offers) => offers.creator)` |
| `assets` | Yes | `Asset[]` | `@OneToMany(() => Asset, (assets) => assets.user)` |
| `socialMedia` | Yes | `SocialMedia[]` | `@OneToMany(() => SocialMedia, (socialMedia) => socialMedia.user)` |
| `downloads` | Yes | `Download[]` | `@OneToMany(() => Download, (download) => download.user)` |
| `transactions` | Yes | `Transaction[]` | `@OneToMany(() => Transaction, (transaction) => transaction.user)` |
| `comments` | Yes | `Comment[]` | `@OneToMany(() => Comment, (comment) => comment.user)` |
| `commentFlags` | Yes | `CommentFlag[]` | `@OneToMany(() => CommentFlag, (commentFlag) => commentFlag.user)` |
| `assetFlags` | Yes | `AssetFlag[]` | `@OneToMany(() => AssetFlag, (assetFlag) => assetFlag.user)` |
| `commentVotes` | Yes | `CommentVote[]` | `@OneToMany(() => CommentVote, (commentVote) => commentVote.user)` |
| `notifications` | Yes | `Notification[]` | `@OneToMany(() => Notification, (notification) => notification.user)` |
| `listingFlags` | Yes | `ListingFlag[]` | `@OneToMany(() => ListingFlag, (listingFlag) => listingFlag.user)` |
| `payTokens` | Yes | `PayToken[]` | `@OneToMany(() => PayToken, (payToken) => payToken.user)` |
| `whitelistRequests` | Yes | `WhitelistRequest[]` | `@OneToMany(() => WhitelistRequest, (whitelistRequests) => whitelistRequests.user)` |
| `shares` | Yes | `Share[]` | `@OneToMany(() => Share, (shares) => shares.user)` |
| `billingSubscription` | Yes | `BillingSubscription` | `@OneToOne(() => BillingSubscription, (bs) => bs.user)` |
| `userIndex` | Yes | `UserIndex` | `@OneToOne(() => UserIndex, (userIndex) => userIndex.user)` |
| `isSocialLogin` | Yes | `boolean` | `@Column({ name: 'is_social_login', default: false, })` |
| `auth0Sub` | Yes | `string` | `@Column('character varying', { name: 'auth0_sub', nullable: true })` |
| `viralScore` | Yes | `number` | `@Column('float', { name: 'viral_score', nullable: true, default: 0 })` |
| `viralScoreUpdatedAt` | Yes | `Date` | `@Column('timestamptz', { name: 'viral_score_updated_at', nullable: true })` |
| `isAgent` | Yes | `boolean` | `@Column('boolean', { name: 'is_agent', default: false })` |
| `agentDescription` | Yes | `string` | `@Column('character varying', { name: 'agent_description', nullable: true })` |
| `callbackUrl` | Yes | `string` | `@Column('character varying', { name: 'callback_url', nullable: true })` |
| `operatorId` | Yes | `string` | `@Column('uuid', { name: 'operator_id', nullable: true })` |
| `operator` | Yes | `User` | `@ManyToOne(() => User, { nullable: true })`<br>`@JoinColumn({ name: 'operator_id', referencedColumnName: 'userId' })` |
| `reputationScore` | Yes | `number` | `@Column('float', { name: 'reputation_score', nullable: true, default: 0.5 })` |
| `redemptionMode` | Yes | `string` | `@Column({ name: 'redemption_mode', type: 'varchar', length: 10, default: 'auto', })` |
| `emailVerificationDeadline` | Yes | `Date` | `@Column('timestamptz', { name: 'email_verification_deadline', nullable: true, })` |
| `paypalBillingAgreementId` | Yes | `string` | `@Column('character varying', { name: 'paypal_billing_agreement_id', nullable: true, })` |
| `profileCounts` | Yes | `UserProfileCounts` | `@OneToOne(() => UserProfileCounts, (counts) => counts.user)` |
| `lastHomeCheck` | Yes | `Date` | `@Column('timestamptz', { name: 'last_home_check', nullable: true })` |
| `createdAt` | Yes | `Date` | `@CreateDateColumn({ name: 'created_at' })` |
| `updatedAt` | Yes | `Date` | `@UpdateDateColumn({ name: 'updated_at' })` |
| `deletedAt` | Yes | `Date` | `@DeleteDateColumn({ name: 'deleted_at' })` |

## class User2faCodeDTO

- Source: `src/user/dto/user2faQrcode.dto.ts:3`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `qrcode` | Yes | `string` |  |
| `secret` | Yes | `string` |  |

## class UserChangePassDTO

- Source: `src/user/dto/userChangePass.dto.ts:8`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `token` | Yes | `string` | `@IsString` |
| `password` | Yes | `string` | `@IsStrongPassword(IS_STRONG_PASSWORD_OPTIONS)`<br>`@MaxLength(PASSWORD_RULES.maxLength)` |

## class UserChangePasswordDTO

- Source: `src/user/dto/userChangePassword.dto.ts:8`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `currentPassword` | Yes | `string` | `@IsString`<br>`@MaxLength(PASSWORD_RULES.maxLength)` |
| `newPassword` | Yes | `string` | `@IsStrongPassword(IS_STRONG_PASSWORD_OPTIONS)`<br>`@MaxLength(PASSWORD_RULES.maxLength)` |

## class UserEmailDTO

- Source: `src/user/dto/userEmail.dto.ts:4`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `email` | Yes | `string` | `@IsEmail` |

## class UserFeedHistory

- Source: `src/user-feed-queue/entities/user-feed-history.entity.ts:18`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `id` | Yes | `string` | `@PrimaryColumn({ type: 'uuid' })` |
| `userId` | Yes | `string` | `@Column({ name: 'user_id', type: 'uuid' })` |
| `user` | Yes | `User` | `@ManyToOne(() => User, { onDelete: 'CASCADE' })`<br>`@JoinColumn({ name: 'user_id', referencedColumnName: 'userId' })` |
| `targetType` | Yes | `FeedTargetType` | `@Column({ name: 'target_type', type: 'text' })` |
| `targetId` | Yes | `string` | `@Column({ name: 'target_id', type: 'uuid' })` |
| `viewedAt` | Yes | `Date` | `@CreateDateColumn({ name: 'viewed_at', type: 'timestamptz' })` |
| `__hydratedTarget` | No | `Folder \| Asset \| null` |  |

## class UserFeedHistoryPageDto

- Source: `src/user-feed-queue/dto/user-feed-queue.dto.ts:14`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `entries` | Yes | `UserFeedHistory[]` |  |
| `nextCursor` | No | `string` |  |

## class UserFeedQueueDto

- Source: `src/user-feed-queue/dto/user-feed-queue.dto.ts:5`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `entries` | Yes | `UserFeedQueueEntry[]` |  |
| `activeEntryId` | Yes | `string \| null` |  |

## class UserFeedQueueEntry

- Source: `src/user-feed-queue/entities/user-feed-queue-entry.entity.ts:19`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `id` | Yes | `string` | `@PrimaryColumn({ type: 'uuid' })` |
| `userId` | Yes | `string` | `@Column({ name: 'user_id', type: 'uuid' })` |
| `user` | Yes | `User` | `@ManyToOne(() => User, { onDelete: 'CASCADE' })`<br>`@JoinColumn({ name: 'user_id', referencedColumnName: 'userId' })` |
| `targetType` | Yes | `FeedTargetType` | `@Column({ name: 'target_type', type: 'text' })` |
| `targetId` | Yes | `string` | `@Column({ name: 'target_id', type: 'uuid' })` |
| `rank` | Yes | `string` | `@Column({ type: 'text' })` |
| `createdAt` | Yes | `Date` | `@CreateDateColumn({ name: 'created_at', type: 'timestamptz' })` |
| `updatedAt` | Yes | `Date` | `@UpdateDateColumn({ name: 'updated_at', type: 'timestamptz' })` |
| `__hydratedTarget` | No | `Folder \| Asset \| null` |  |

## class UserFeedQueueState

- Source: `src/user-feed-queue/entities/user-feed-queue-state.entity.ts:6`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `userId` | Yes | `string` | `@PrimaryColumn({ name: 'user_id', type: 'uuid' })` |
| `user` | Yes | `User` | `@ManyToOne(() => User, { onDelete: 'CASCADE' })`<br>`@JoinColumn({ name: 'user_id', referencedColumnName: 'userId' })` |
| `activeEntryId` | Yes | `string \| null` | `@Column({ name: 'active_entry_id', type: 'uuid', nullable: true })` |
| `activeEntry` | Yes | `UserFeedQueueEntry \| null` | `@ManyToOne(() => UserFeedQueueEntry, { onDelete: 'SET NULL', nullable: true })`<br>`@JoinColumn({ name: 'active_entry_id' })` |
| `updatedAt` | Yes | `Date` | `@UpdateDateColumn({ name: 'updated_at', type: 'timestamptz' })` |

## class UserFollowDTO

- Source: `src/user/dto/userFollow.dto.ts:4`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `message` | Yes | `string` | `@IsString` |
| `isFollowed` | Yes | `boolean` | `@IsBoolean` |

## class UserIndex

- Source: `src/user/entities/userIndex.entity.ts:11`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `id` | Yes | `string` | `@PrimaryGeneratedColumn('increment', { type: 'bigint', name: 'id' })` |
| `userId` | Yes | `string \| null` | `@Column('uuid', { name: 'user_id', nullable: true, unique: true })` |
| `user` | Yes | `User` | `@OneToOne(() => User, (user) => user.userIndex, { onDelete: 'SET NULL' })`<br>`@JoinColumn([{ name: 'user_id', referencedColumnName: 'userId' }])` |
| `createdAt` | Yes | `Date` | `@CreateDateColumn({ name: 'created_at' })` |

## class UserLimitResponseDTO

- Source: `src/user/dto/userLimitResponse.dto.ts:3`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `isLimitReached` | Yes | `boolean` |  |
| `currentUserCount` | Yes | `number` |  |
| `maxLimit` | Yes | `number` |  |
| `message` | No | `string` |  |

## class UserLoginDTO

- Source: `src/user/dto/userLogin.dto.ts:4`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `email` | Yes | `string` | `@IsEmail` |
| `password` | Yes | `string` |  |
| `code` | No | `string` | `@IsOptional`<br>`@MinLength(6)`<br>`@MaxLength(6)` |

## class UserLoginResponse

- Source: `src/user/dto/userLoginReponse.dto.ts:4`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `message` | Yes | `string` |  |
| `token` | No | `string` |  |
| `user` | No | `PrivateUser` |  |

## type UserLoginTransportResult

- Source: `src/user/user-login.transport.ts:7`
- Type: `UserLoginResponse & { [USER_LOGIN_SET_COOKIE_HEADERS]?: string[]; }`

## class UserNetworkDTO

- Source: `src/user/dto/userNetwork.dto.ts:3`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `followings` | Yes | `number` |  |
| `followers` | Yes | `number` |  |

## class UserProfileCounts

- Source: `src/user/entities/user-profile-counts.entity.ts:4`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `userId` | Yes | `string` | `@PrimaryColumn({ name: 'user_id', type: 'uuid' })` |
| `user` | Yes | `User` | `@OneToOne(() => User, { onDelete: 'CASCADE' })`<br>`@JoinColumn({ name: 'user_id' })` |
| `listingsCount` | Yes | `number` | `@Column({ name: 'listings_count', type: 'int', default: 0 })` |
| `likesCount` | Yes | `number` | `@Column({ name: 'likes_count', type: 'int', default: 0 })` |
| `favoritesCount` | Yes | `number` | `@Column({ name: 'favorites_count', type: 'int', default: 0 })` |
| `receivedOffersCount` | Yes | `number` | `@Column({ name: 'received_offers_count', type: 'int', default: 0 })` |
| `sentOffersCount` | Yes | `number` | `@Column({ name: 'sent_offers_count', type: 'int', default: 0 })` |
| `bidsCount` | Yes | `number` | `@Column({ name: 'bids_count', type: 'int', default: 0 })` |
| `payTokensCount` | Yes | `number` | `@Column({ name: 'pay_tokens_count', type: 'int', default: 0 })` |
| `referralsCount` | Yes | `number` | `@Column({ name: 'referrals_count', type: 'int', default: 0 })` |
| `followerCount` | Yes | `number` | `@Column({ name: 'follower_count', type: 'int', default: 0 })` |
| `followingCount` | Yes | `number` | `@Column({ name: 'following_count', type: 'int', default: 0 })` |
| `totalSalesCount` | Yes | `number` | `@Column({ name: 'total_sales_count', type: 'int', default: 0 })` |
| `totalSalesVolume` | Yes | `number` | `@Column({ name: 'total_sales_volume', type: 'numeric', precision: 12, scale: 2, default: 0 })` |
| `purchaseCount` | Yes | `number` | `@Column({ name: 'purchase_count', type: 'int', default: 0 })` |
| `commentCount` | Yes | `number` | `@Column({ name: 'comment_count', type: 'int', default: 0 })` |

## class UserSignatureDTO

- Source: `src/user/dto/userSignature.dto.ts:3`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `hash_buffer` | Yes | `string` |  |
| `r` | Yes | `string` |  |
| `s` | Yes | `string` |  |
| `v` | Yes | `number` |  |

## class UserSignupDTO

- Source: `src/user/dto/userSignup.dto.ts:14`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `email` | Yes | `string` | `@IsEmail` |
| `password` | Yes | `string` | `@IsStrongPassword(IS_STRONG_PASSWORD_OPTIONS)`<br>`@MaxLength(PASSWORD_RULES.maxLength)` |
| `userName` | Yes | `string` | `@IsString` |
| `referrerCode` | Yes | `string` | `@IsString`<br>`@IsOptional` |
| `bio` | Yes | `string` | `@IsString`<br>`@IsOptional` |
| `avatar` | Yes | `string` | `@IsString`<br>`@IsOptional` |
| `twitter` | Yes | `string` | `@IsString`<br>`@IsOptional` |
| `instagram` | Yes | `string` | `@IsString`<br>`@IsOptional` |
| `website` | Yes | `string` | `@IsString`<br>`@IsOptional` |
| `banner` | Yes | `string` | `@IsString`<br>`@IsOptional` |

## class UserStatus

- Source: `src/user/entities/userStatus.entity.ts:14`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `userStatusId` | Yes | `number` | `@PrimaryGeneratedColumn({ name: 'user_status_id' })` |
| `name` | Yes | `string` | `@Column('character varying', { name: 'name' })` |
| `users` | Yes | `User[]` | `@OneToMany(() => User, (users) => users.userStatus)` |
| `createdAt` | Yes | `Date` | `@CreateDateColumn({ name: 'created_at' })` |
| `updatedAt` | Yes | `Date` | `@UpdateDateColumn({ name: 'updated_at' })` |
| `deletedAt` | Yes | `Date` | `@DeleteDateColumn({ name: 'deleted_at' })` |

## type UserStatusType

- Source: `src/utils/types.ts:2`
- Type: `'active' \| 'whitelist' \| 'blacklist'`

## class UserUpdateAccountDTO

- Source: `src/user/dto/userUpdateAccount.dto.ts:4`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `bio` | Yes | `string` | `@IsString`<br>`@IsOptional` |
| `email` | Yes | `string` | `@IsString`<br>`@IsOptional` |
| `twitter` | Yes | `string` | `@IsString`<br>`@IsOptional` |
| `instagram` | Yes | `string` | `@IsString`<br>`@IsOptional` |
| `website` | Yes | `string` | `@IsString`<br>`@IsOptional` |

## class UserUpdateNotificationSettingDTO

- Source: `src/user/dto/userUpdateNotificationSetting.dto.ts:3`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `updateList` | Yes | `string[]` |  |

## class UserWallet

- Source: `src/user/entities/userWallet.entity.ts:13`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `userWalletId` | Yes | `string` | `@PrimaryGeneratedColumn('uuid', { name: 'user_wallet_id' })` |
| `address` | Yes | `string` | `@Column('character varying', { name: 'wallet_address', unique: true })` |
| `signature` | Yes | `string` | `@Column('character varying', { name: 'signature' })` |
| `userId` | Yes | `string` | `@Column({ name: 'user_id' })` |
| `user` | Yes | `User` | `@ManyToOne(() => User, (user) => user.userWallets)`<br>`@JoinColumn([{ name: 'user_id', referencedColumnName: 'userId' }])` |
| `isVerified` | Yes | `boolean` | `@Column('boolean', { name: 'is_verified', default: false })` |
| `createdAt` | Yes | `Date` | `@CreateDateColumn({ name: 'created_at' })` |
| `updatedAt` | Yes | `Date` | `@UpdateDateColumn({ name: 'updated_at' })` |
| `deletedAt` | Yes | `Date` | `@DeleteDateColumn({ name: 'deleted_at' })` |

## class UserWhitelistRequestDTO

- Source: `src/activity/dto/userWhitelistRequest.dto.ts:4`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `description` | Yes | `string` | `@IsString` |

## class ValidatePayPalCaptureDTO

- Source: `src/paypal/dto/validatePayPalCapture.dto.ts:4`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `orderId` | Yes | `string` | `@IsString` |
| `price` | Yes | `number` | `@IsNumber({ maxDecimalPlaces: 2 })`<br>`@Min(0)` |

## interface ValidationFieldError

- Source: `src/utils/agent-validation.pipe.ts:43`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `field` | Yes | `string` |  |
| `constraint` | Yes | `string` |  |
| `message` | Yes | `string` |  |
| `hint` | No | `string` |  |

## class ValidationStringResponseDTO

- Source: `src/user/dto/validationStringResponse.dto.ts:3`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `validationString` | Yes | `string` |  |
| `message` | Yes | `string` |  |

## interface ValkeyLike
_Minimal interface for the Valkey/Redis client used by this plugin. Compatible with both node-redis v4 (`createClient`) and ioredis._

- Source: `src/auth/plugins/device-ownership.plugin.ts:8`

_No declared properties._

## class VerifyMetamaskDTO

- Source: `src/user/dto/verifyMetamask.dto.ts:4`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `address` | Yes | `string` | `@IsEthereumAddress` |
| `signature` | Yes | `string` | `@IsString` |

## class VerifyMetamaskResponseDTO

- Source: `src/user/dto/verifyMetamaskResponse.dto.ts:3`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `result` | Yes | `boolean` |  |
| `message` | Yes | `string` |  |

## class View

- Source: `src/activity/entities/view.entity.ts:15`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `viewId` | Yes | `string` | `@PrimaryGeneratedColumn('uuid', { name: 'view_id' })` |
| `listingId` | Yes | `string` | `@Column({ name: 'listing_id' })` |
| `listing` | Yes | `Listing` | `@ManyToOne(() => Listing, (listing) => listing.views)`<br>`@JoinColumn({ name: 'listing_id', referencedColumnName: 'listingId' })` |
| `userId` | Yes | `string` | `@Column({ name: 'user_id' })` |
| `user` | Yes | `User` | `@ManyToOne(() => User, (tag) => tag.views)`<br>`@JoinColumn({ name: 'user_id', referencedColumnName: 'userId' })` |
| `createdAt` | Yes | `Date` | `@CreateDateColumn({ name: 'created_at' })` |

## class VisibilityChangePreviewDTO

- Source: `src/listing/dto/visibility-change-preview.dto.ts:16`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `affectedPublicFolders` | Yes | `AffectedFolderDTO[]` |  |
| `affectedLibraryCount` | Yes | `number` |  |

## enum VoteType

- Source: `src/activity/utils/types.ts:1`

| Member | Value |
|---|---|
| `UPVOTE` | `'upvote'` |
| `DOWNVOTE` | `'downvote'` |

## class Waitlist

- Source: `src/user/entities/waitlist.entity.ts:15`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `id` | Yes | `string` | `@PrimaryGeneratedColumn('uuid')` |
| `email` | Yes | `string` | `@Column('character varying', { name: 'email', length: 255 })` |
| `useCase` | Yes | `string` | `@Column('character varying', { name: 'use_case', length: 255, nullable: true, })` |
| `profession` | Yes | `string` | `@Column('character varying', { name: 'profession', length: 255, nullable: true, })` |
| `workEmail` | Yes | `string` | `@Column('character varying', { name: 'work_email', length: 255, nullable: true, })` |
| `socialMedia` | Yes | `string` | `@Column('character varying', { name: 'social_links', length: 500, nullable: true, })` |
| `status` | Yes | `WaitlistStatus` | `@Column({ name: 'status', type: 'enum', enum: WaitlistStatus, default: WaitlistStatus.PENDING, })` |
| `referrer` | Yes | `User` | `@ManyToOne(() => User, { nullable: true })`<br>`@JoinColumn([{ name: 'referrer_id', referencedColumnName: 'userId' }])` |
| `referrerId` | Yes | `string` | `@Column('uuid', { name: 'referrer_id', nullable: true })` |
| `createdAt` | Yes | `Date` | `@CreateDateColumn({ name: 'created_at' })` |

## enum WaitlistStatus

- Source: `src/user/utils/waitlistStatus.ts:1`

| Member | Value |
|---|---|
| `PENDING` | `'PENDING'` |
| `APPROVED` | `'APPROVED'` |
| `PROCESSING` | `'PROCESSING'` |
| `ONBOARDED` | `'ONBOARDED'` |

## class WalletAddressDTO

- Source: `src/user/dto/walletAddress.dto.ts:4`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `address` | Yes | `string` | `@IsEthereumAddress` |

## enum WalletType

- Source: `src/billing/billing.enums.ts:19`

| Member | Value |
|---|---|
| `SUBSCRIPTION` | `'subscription'` |
| `TOPUP` | `'topup'` |

## class WalletVerifiedResponseDTO

- Source: `src/user/dto/walletVerifiedResponse.dto.ts:3`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `isVerified` | Yes | `boolean` |  |
| `message` | Yes | `string` |  |

## class WebhookEndpoint

- Source: `src/webhook/entities/webhook-endpoint.entity.ts:13`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `id` | Yes | `string` | `@PrimaryGeneratedColumn('uuid')` |
| `userId` | Yes | `string` | `@Column({ name: 'user_id' })` |
| `user` | Yes | `User` | `@ManyToOne(() => User)`<br>`@JoinColumn({ name: 'user_id' })` |
| `url` | Yes | `string` | `@Column({ length: 500 })` |
| `secret` | Yes | `string` | `@Column({ length: 64 })` |
| `events` | Yes | `string[]` | `@Column('text', { array: true })` |
| `active` | Yes | `boolean` | `@Column({ default: true })` |
| `createdAt` | Yes | `Date` | `@CreateDateColumn({ name: 'created_at' })` |
| `updatedAt` | Yes | `Date` | `@UpdateDateColumn({ name: 'updated_at' })` |

## enum WebhookEventType

- Source: `src/webhook/utils/types.ts:1`

| Member | Value |
|---|---|
| `LISTING_SOLD` | `'listing.sold'` |
| `LISTING_UPDATED` | `'listing.updated'` |
| `LISTING_DELETED` | `'listing.deleted'` |
| `LISTING_TRANSFERRED` | `'listing.transferred'` |
| `DOWNLOAD_COMPLETED` | `'download.completed'` |
| `OFFER_RECEIVED` | `'offer.received'` |
| `OFFER_ACCEPTED` | `'offer.accepted'` |
| `OFFER_REJECTED` | `'offer.rejected'` |
| `OFFER_COUNTERED` | `'offer.countered'` |
| `PAYMENT_RECEIVED` | `'payment.received'` |
| `POINTS_EARNED` | `'points.earned'` |
| `MENTION_CREATED` | `'mention.created'` |
| `LISTING_PUBLISHED` | `'listing.published'` |
| `LISTING_PUBLISH_FAILED` | `'listing.publish_failed'` |
| `LISTING_PROCESSING_FAILED` | `'listing.processing_failed'` |
| `LISTING_MINTED` | `'listing.minted'` |
| `LISTING_REJECTED` | `'listing.rejected'` |
| `LISTING_DISCARDED` | `'listing.discarded'` |
| `LISTING_PENDING_APPROVAL` | `'listing.pending_approval'` |
| `ASSET_LIKED` | `'asset.liked'` |
| `ASSET_COMMENTED` | `'asset.commented'` |
| `NEW_FOLLOWER` | `'user.new_follower'` |
| `PRICE_CHANGE` | `'listing.price_change'` |
| `BID_RECEIVED` | `'bid.received'` |

## interface WebhookTestResponse

- Source: `src/agent/dto/webhook-test.dto.ts:1`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `delivered` | Yes | `boolean` |  |
| `status_code` | Yes | `number \| null` |  |
| `response_time_ms` | Yes | `number \| null` |  |
| `callback_url` | Yes | `string` |  |

## class WhitelistRequest

- Source: `src/activity/entities/whitelistRequest.entity.ts:15`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `whitelistRequestId` | Yes | `string` | `@PrimaryGeneratedColumn('uuid', { name: 'whitelist_request_id' })` |
| `userId` | Yes | `string` | `@Column({ name: 'user_id' })` |
| `user` | Yes | `User` | `@ManyToOne(() => User, (user) => user.whitelistRequests)`<br>`@JoinColumn({ name: 'user_id', referencedColumnName: 'userId' })` |
| `description` | Yes | `string` | `@Column('character varying', { name: 'description', nullable: true })` |
| `rejectReason` | Yes | `string` | `@Column('character varying', { name: 'reject_reason', nullable: true })` |
| `isChecked` | Yes | `boolean` | `@Column({ name: 'is_checked', default: false, })` |
| `createdAt` | Yes | `Date` | `@CreateDateColumn({ name: 'created_at' })` |
| `updatedAt` | Yes | `Date` | `@UpdateDateColumn({ name: 'updated_at' })` |
| `deletedAt` | Yes | `Date` | `@DeleteDateColumn({ name: 'deleted_at' })` |

## class WhitelistUserDTO

- Source: `src/activity/dto/whitelistUser.dto.ts:4`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `token` | Yes | `string` | `@IsString` |

## interface WsPayload

- Source: `src/notifications/types/payloads.ts:12`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `title` | Yes | `string` |  |
| `message` | Yes | `string` |  |
| `link` | No | `string` |  |

## interface ZipManifestSummary

- Source: `src/listing/dto/zip-manifest-summary.dto.ts:61`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `version` | Yes | `number` |  |
| `generatedAt` | Yes | `string` |  |
| `totalFiles` | Yes | `number` |  |
| `totalSizeBytes` | Yes | `number` |  |
| `types` | Yes | `Record< string, { count: number; sizeBytes: number; extensions: string[] } >` |  |

## class ZipManifestSummaryType

- Source: `src/listing/dto/zip-manifest-summary.dto.ts:39`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `version` | Yes | `number` |  |
| `generatedAt` | Yes | `string` |  |
| `totalFiles` | Yes | `number` |  |
| `totalSizeBytes` | Yes | `number` |  |
| `types` | Yes | `ZipManifestTypes` |  |
| `manifestUrl` | Yes | `string` |  |

## class ZipManifestTypeBucket

- Source: `src/listing/dto/zip-manifest-summary.dto.ts:3`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `count` | Yes | `number` |  |
| `sizeBytes` | Yes | `number` |  |
| `extensions` | Yes | `string[]` |  |

## class ZipManifestTypes

- Source: `src/listing/dto/zip-manifest-summary.dto.ts:15`

| Field | Required | Type | Validators / decorators |
|---|---:|---|---|
| `image` | Yes | `ZipManifestTypeBucket` |  |
| `video` | Yes | `ZipManifestTypeBucket` |  |
| `audio` | Yes | `ZipManifestTypeBucket` |  |
| `font` | Yes | `ZipManifestTypeBucket` |  |
| `document` | Yes | `ZipManifestTypeBucket` |  |
| `threeD` | Yes | `ZipManifestTypeBucket` |  |
| `other` | Yes | `ZipManifestTypeBucket` |  |

