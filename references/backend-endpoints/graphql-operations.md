# GraphQL Operation Inventory

Generated from backend commit `c50dd33d` on 2026-05-05.

> Backend awareness only. Agents must not use GraphQL. Do not copy operation names, queries, mutations, schemas, or `/graphql` examples from this file into Wondermint skill files; the MVP skill is REST-only.

The backend mounts GraphQL through `GraphQLModule` with `autoSchemaFile: true`. This file inventories resolver operations from source decorators for maintainers only.

Total GraphQL operations: **305**.

| Type | Operation | Handler | Return type | Source |
|---|---|---|---|---|
| Mutation | `acceptCounterOffer` | `MarketplaceMutation.acceptCounterOffer` | `Promise<CustomMessageDTO>` | `src/marketplace/marketplace.mutation.ts:83` |
| Mutation | `acceptOffer` | `MarketplaceMutation.acceptOffer` | `Promise<CustomMessageDTO>` | `src/marketplace/marketplace.mutation.ts:50` |
| Mutation | `addComment` | `ActivityMutation.addComment` | `Promise<CommentDTO>` | `src/activity/activity.mutation.ts:170` |
| Mutation | `addCommentFlag` | `ActivityMutation.addCommentFlag` | `Promise<CustomMessageDTO>` | `src/activity/activity.mutation.ts:204` |
| Mutation | `addCommentVote` | `ActivityMutation.addCommentVote` | `Promise<CommentVote>` | `src/activity/activity.mutation.ts:193` |
| Mutation | `addListingFlag` | `ListingMutation.addListingFlag` | `Promise<CustomMessageDTO>` | `src/listing/listing.mutation.ts:345` |
| Mutation | `addOrUpdateCategory` | `ListingMutation.addOrUpdateCategory` | `Promise<Category>` | `src/listing/listing.mutation.ts:325` |
| Mutation | `addOrUpdateQA` | `UserMutation.addOrUpdateQA` | `Promise<QA>` | `src/user/user.mutation.ts:347` |
| Mutation | `addOrUpdateQuestionType` | `UserMutation.addOrUpdateQuestionType` | `Promise<QuestionType>` | `src/user/user.mutation.ts:363` |
| Mutation | `addPayToken` | `ListingMutation.addPayToken` | `Promise<CustomMessageDTO>` | `src/listing/listing.mutation.ts:278` |
| Mutation | `addPointType` | `PointMutation.addPointType` | `Promise<PointType>` | `src/point/point.mutation.ts:14` |
| Mutation | `addToWaitlist` | `UserMutation.addToWaitlist` | `Promise<CustomMessageDTO>` | `src/user/user.mutation.ts:126` |
| Mutation | `addTransaction` | `ListingMutation.addTransaction` | `Promise<CustomMessageDTO>` | `src/listing/listing.mutation.ts:174` |
| Mutation | `adminApproveWaitlist` | `UserMutation.adminApproveWaitlist` | `Promise<CustomMessageDTO>` | `src/user/user.mutation.ts:393` |
| Mutation | `adminApproveWaitlists` | `UserMutation.adminApproveWaitlists` | `Promise<CustomMessageDTO>` | `src/user/user.mutation.ts:402` |
| Mutation | `adminCancelSubscription` | `BillingAdminMutation.adminCancelSubscription` | `Promise<boolean>` | `src/billing/billing-admin.mutation.ts:21` |
| Mutation | `adminGrantSubscription` | `BillingAdminMutation.adminGrantSubscription` | `Promise<boolean>` | `src/billing/billing-admin.mutation.ts:13` |
| Mutation | `adminLogin` | `UserMutation.adminLogin` | `Promise<AdminLoginResponse>` | `src/user/user.mutation.ts:138` |
| Mutation | `approveListing` | `ListingMutation.approveListing` | `Promise<ListingDTO>` | `src/listing/listing.mutation.ts:156` |
| Mutation | `authorizePayPalPayment` | `PayPalMutation.authorizePayPalPayment` | `Promise<string>` | `src/paypal/paypal.mutation.ts:75` |
| Mutation | `backfillSearchIndex` | `SearchResolver.backfillSearchIndex` | `Promise<boolean>` | `src/search/search.resolver.ts:180` |
| Mutation | `bulkAddListingsToFolder` | `FolderMutation.bulkAddListingsToFolder` | `Promise<BulkAddResultType>` | `src/folder/resolvers/folder.mutation.ts:198` |
| Mutation | `bulkRemoveListingsFromFolder` | `FolderMutation.bulkRemoveListingsFromFolder` | `Promise<BulkRemoveResultType>` | `src/folder/resolvers/folder.mutation.ts:207` |
| Mutation | `calcPayPalEstimate` | `PayPalMutation.calcPayPalEstimate` | `Promise<number>` | `src/paypal/paypal.mutation.ts:106` |
| Mutation | `cancelBuyAsset` | `MarketplaceMutation.cancelBuyAsset` | `Promise<CustomMessageDTO>` | `src/marketplace/marketplace.mutation.ts:63` |
| Mutation | `cancelCreditTopUp` | `BillingMutation.cancelCreditTopUp` | `Promise<boolean>` | `src/billing/billing.mutation.ts:164` |
| Mutation | `cancelOffer` | `MarketplaceMutation.cancelOffer` | `Promise<CustomMessageDTO>` | `src/marketplace/marketplace.mutation.ts:37` |
| Mutation | `cancelPendingDowngrade` | `BillingMutation.cancelPendingDowngrade` | `Promise<boolean>` | `src/billing/billing.mutation.ts:136` |
| Mutation | `cancelSubscription` | `BillingMutation.cancelSubscription` | `Promise<boolean>` | `src/billing/billing.mutation.ts:54` |
| Mutation | `clearFeedHistory` | `UserFeedQueueMutationResolver.clearFeedHistory` | `Promise<number>` | `src/user-feed-queue/resolvers/user-feed-queue.mutation.ts:60` |
| Mutation | `clearQueue` | `UserFeedQueueMutationResolver.clearQueue` | `Promise<number>` | `src/user-feed-queue/resolvers/user-feed-queue.mutation.ts:47` |
| Mutation | `confirmOwnershipPurchase` | `PayPalMutation.confirmOwnershipPurchase` | `Promise<ConfirmOwnershipPurchaseResponseDTO>` | `src/paypal/paypal.mutation.ts:137` |
| Mutation | `copyShareLink` | `ActivityMutation.copyShareLink` | `Promise<CustomMessageDTO>` | `src/activity/activity.mutation.ts:118` |
| Mutation | `counterOffer` | `MarketplaceMutation.counterOffer` | `Promise<OfferDTO>` | `src/marketplace/marketplace.mutation.ts:74` |
| Mutation | `createAiModel` | `AiModelMutation.createAiModel` | `Promise<AiModelResponseDTO>` | `src/ai-model/ai-model.mutation.ts:15` |
| Mutation | `createBillingPortalSession` | `BillingMutation.createBillingPortalSession` | `Promise<CheckoutUrlDTO>` | `src/billing/billing.mutation.ts:180` |
| Mutation | `createFolder` | `FolderMutation.createFolder` | `Promise<Folder>` | `src/folder/resolvers/folder.mutation.ts:28` |
| Mutation | `createOwnershipAuthorizeLink` | `PayPalMutation.createOwnershipAuthorizeLink` | `Promise<BuyLinkDTO>` | `src/paypal/paypal.mutation.ts:117` |
| Mutation | `createPaymentMethodUpdateFlow` | `BillingMutation.createPaymentMethodUpdateFlow` | `Promise<CheckoutUrlDTO>` | `src/billing/billing.mutation.ts:170` |
| Mutation | `createPayPalBuyLink` | `PayPalMutation.createPayPalBuyLink` | `Promise<BuyLinkDTO>` | `src/paypal/paypal.mutation.ts:49` |
| Mutation | `createPayPalDownloadLicenseLink` | `PayPalMutation.createPayPalDownloadLicenseLink` | `Promise<BuyLinkDTO>` | `src/paypal/paypal.mutation.ts:61` |
| Mutation | `createShare` | `ActivityMutation.createShare` | `Promise<string>` | `src/activity/activity.mutation.ts:92` |
| Mutation | `createSubscriptionCheckout` | `BillingMutation.createSubscriptionCheckout` | `Promise<CheckoutUrlDTO>` | `src/billing/billing.mutation.ts:17` |
| Mutation | `createUploadPresignedUrl` | `ListingMutation.createUploadPresignedUrl` | `Promise<CreateUploadPresignedUrlResponseDTO>` | `src/listing/listing.mutation.ts:206` |
| Mutation | `createUserPresignedUrl` | `UserMutation.createUserPresignedUrl` | `Promise<CreateUserPresignedUrlResponseDTO>` | `src/user/user.mutation.ts:336` |
| Mutation | `deleteAiModel` | `AiModelMutation.deleteAiModel` | `Promise<boolean>` | `src/ai-model/ai-model.mutation.ts:31` |
| Mutation | `deleteAssetFlag` | `ListingMutation.deleteAssetFlag` | `Promise<CustomMessageDTO>` | `src/listing/listing.mutation.ts:397` |
| Mutation | `deleteComment` | `ActivityMutation.deleteComment` | `Promise<CustomMessageDTO>` | `src/activity/activity.mutation.ts:182` |
| Mutation | `deleteFeedHistoryEntry` | `UserFeedQueueMutationResolver.deleteFeedHistoryEntry` | `Promise<boolean>` | `src/user-feed-queue/resolvers/user-feed-queue.mutation.ts:52` |
| Mutation | `deleteFile` | `ListingMutation.deleteFile` | `Promise<CustomMessageDTO>` | `src/listing/listing.mutation.ts:221` |
| Mutation | `deleteFolder` | `FolderMutation.deleteFolder` | `Promise<boolean>` | `src/folder/resolvers/folder.mutation.ts:45` |
| Mutation | `dequeueEntry` | `UserFeedQueueMutationResolver.dequeueEntry` | `Promise<boolean>` | `src/user-feed-queue/resolvers/user-feed-queue.mutation.ts:23` |
| Mutation | `downgradeSubscription` | `BillingMutation.downgradeSubscription` | `Promise<boolean>` | `src/billing/billing.mutation.ts:92` |
| Mutation | `enqueueTarget` | `UserFeedQueueMutationResolver.enqueueTarget` | `Promise<UserFeedQueueEntry>` | `src/user-feed-queue/resolvers/user-feed-queue.mutation.ts:13` |
| Mutation | `followFolder` | `FolderMutation.followFolder` | `Promise<boolean>` | `src/folder/resolvers/folder.mutation.ts:178` |
| Mutation | `generateRegistrationTokens` | `UserMutation.generateRegistrationTokens` | `Promise<CustomMessageDTO>` | `src/user/user.mutation.ts:411` |
| Mutation | `hideCommentAndFlags` | `ActivityMutation.hideCommentAndFlags` | `Promise<CustomMessageDTO>` | `src/activity/activity.mutation.ts:226` |
| Mutation | `hideListingAndFlags` | `ListingMutation.hideListingAndFlags` | `Promise<CustomMessageDTO>` | `src/listing/listing.mutation.ts:367` |
| Mutation | `ignoreCommentFlag` | `ActivityMutation.ignoreCommentFlag` | `Promise<CustomMessageDTO>` | `src/activity/activity.mutation.ts:216` |
| Mutation | `ignoreListingFlag` | `ListingMutation.ignoreListingFlag` | `Promise<CustomMessageDTO>` | `src/listing/listing.mutation.ts:357` |
| Mutation | `initListing` | `ListingMutation.initListing` | `Promise<string>` | `src/listing/listing.mutation.ts:54` |
| Mutation | `likeFolder` | `FolderMutation.likeFolder` | `Promise<boolean>` | `src/folder/resolvers/folder.mutation.ts:142` |
| Mutation | `markMentionRead` | `MentionQuery.markMentionRead` | `Promise<boolean>` | `src/mention/mention.query.ts:38` |
| Mutation | `mintListing` | `ListingMutation.mintListing` | `Promise<CustomMessageDTO>` | `src/listing/listing.mutation.ts:72` |
| Mutation | `moveListingToPortfolio` | `FolderMutation.moveListingToPortfolio` | `Promise<boolean>` | `src/folder/resolvers/folder.mutation.ts:54` |
| Mutation | `notificationViewed` | `NotificationsMutation.notificationViewed` | `Promise<CustomMessageDTO>` | `src/notifications/notifications.mutation.ts:13` |
| Mutation | `placeBid` | `AuctionMutation.placeBid` | `Promise<CustomMessageDTO>` | `src/auction/auction.mutation.ts:27` |
| Mutation | `publishListing` | `ListingMutation.publishListing` | `Promise<PublishListingResultDTO>` | `src/listing/listing.mutation.ts:83` |
| Mutation | `purchaseListing` | `ListingMutation.purchaseListing` | `Promise<PurchaseResultDTO>` | `src/listing/listing.mutation.ts:438` |
| Mutation | `recoverComment` | `ActivityMutation.recoverComment` | `Promise<CustomMessageDTO>` | `src/activity/activity.mutation.ts:236` |
| Mutation | `recoverListing` | `ListingMutation.recoverListing` | `Promise<CustomMessageDTO>` | `src/listing/listing.mutation.ts:377` |
| Mutation | `redeemShare` | `ActivityMutation.redeemShare` | `Promise<Share>` | `src/activity/activity.mutation.ts:103` |
| Mutation | `regenerateRegisterPayPalSeller` | `PayPalMutation.regenerateRegisterPayPalSeller` | `Promise<string>` | `src/paypal/paypal.mutation.ts:29` |
| Mutation | `registerListing` | `ListingMutation.registerListing` | `Promise<string>` | `src/listing/listing.mutation.ts:61` |
| Mutation | `registerPayPalSeller` | `PayPalMutation.registerPayPalSeller` | `Promise<string>` | `src/paypal/paypal.mutation.ts:20` |
| Mutation | `rejectListing` | `ListingMutation.rejectListing` | `Promise<ListingDTO>` | `src/listing/listing.mutation.ts:164` |
| Mutation | `rejectUserWhitelistRequest` | `ActivityMutation.rejectUserWhitelistRequest` | `Promise<CustomMessageDTO>` | `src/activity/activity.mutation.ts:150` |
| Mutation | `rejectUserWhitelistRequestByAdmin` | `ActivityMutation.rejectUserWhitelistRequestByAdmin` | `Promise<CustomMessageDTO>` | `src/activity/activity.mutation.ts:160` |
| Mutation | `removeBid` | `AuctionMutation.removeBid` | `Promise<CustomMessageDTO>` | `src/auction/auction.mutation.ts:14` |
| Mutation | `removeCategory` | `ListingMutation.removeCategory` | `Promise<CustomMessageDTO>` | `src/listing/listing.mutation.ts:335` |
| Mutation | `removeListing` | `ListingMutation.removeListing` | `Promise<CustomMessageDTO>` | `src/listing/listing.mutation.ts:184` |
| Mutation | `removeListingFromCollection` | `FolderMutation.removeListingFromCollection` | `Promise<boolean>` | `src/folder/resolvers/folder.mutation.ts:83` |
| Mutation | `removeListingFromPortfolio` | `FolderMutation.removeListingFromPortfolio` | `Promise<boolean>` | `src/folder/resolvers/folder.mutation.ts:64` |
| Mutation | `removeNotification` | `NotificationsMutation.removeNotification` | `Promise<CustomMessageDTO>` | `src/notifications/notifications.mutation.ts:36` |
| Mutation | `removeOffer` | `MarketplaceMutation.removeOffer` | `Promise<CustomMessageDTO>` | `src/marketplace/marketplace.mutation.ts:24` |
| Mutation | `removePayToken` | `ListingMutation.removePayToken` | `Promise<CustomMessageDTO>` | `src/listing/listing.mutation.ts:304` |
| Mutation | `removeQA` | `UserMutation.removeQA` | `Promise<CustomMessageDTO>` | `src/user/user.mutation.ts:355` |
| Mutation | `removeQuestionType` | `UserMutation.removeQuestionType` | `Promise<CustomMessageDTO>` | `src/user/user.mutation.ts:373` |
| Mutation | `removeUnusedFiles` | `ListingMutation.removeUnusedFiles` | `Promise<CustomMessageDTO>` | `src/listing/listing.mutation.ts:257` |
| Mutation | `reorderFolder` | `FolderMutation.reorderFolder` | `Promise<boolean>` | `src/folder/resolvers/folder.mutation.ts:113` |
| Mutation | `reorderFolderListing` | `FolderMutation.reorderFolderListing` | `Promise<boolean>` | `src/folder/resolvers/folder.mutation.ts:97` |
| Mutation | `reorderQueueEntry` | `UserFeedQueueMutationResolver.reorderQueueEntry` | `Promise<boolean>` | `src/user-feed-queue/resolvers/user-feed-queue.mutation.ts:31` |
| Mutation | `requestBulkExport` | `AnalyticsResolver.requestBulkExport` | `Promise<BulkExportStatusDTO>` | `src/analytics/analytics.resolver.ts:186` |
| Mutation | `requestReprocessing` | `ListingMutation.requestReprocessing` | `Promise<CustomMessageDTO>` | `src/listing/listing.mutation.ts:195` |
| Mutation | `resetNegativePoint` | `UserMutation.resetNegativePoint` | `Promise<CustomMessageDTO>` | `src/user/user.mutation.ts:383` |
| Mutation | `resetUser2fa` | `UserMutation.resetUser2fa` | `Promise<CustomMessageDTO>` | `src/user/user.mutation.ts:312` |
| Mutation | `retryDeadLetter` | `OutboxResolver.retryDeadLetter` | `Promise<boolean>` | `src/resilience/outbox/outbox.resolver.ts:29` |
| Mutation | `saveFolder` | `FolderMutation.saveFolder` | `Promise<boolean>` | `src/folder/resolvers/folder.mutation.ts:160` |
| Mutation | `saveListingToCollection` | `FolderMutation.saveListingToCollection` | `Promise<boolean>` | `src/folder/resolvers/folder.mutation.ts:73` |
| Mutation | `saveListingTxHash` | `ListingMutation.saveListingTxHash` | `Promise<CustomMessageDTO>` | `src/listing/listing.mutation.ts:267` |
| Mutation | `savePayToken` | `ListingMutation.savePayToken` | `Promise<CustomMessageDTO>` | `src/listing/listing.mutation.ts:315` |
| Mutation | `savePayTokenTxHash` | `ListingMutation.savePayTokenTxHash` | `Promise<CustomMessageDTO>` | `src/listing/listing.mutation.ts:289` |
| Mutation | `sendMemeToken` | `ListingMutation.sendMemeToken` | `Promise<CustomMessageDTO>` | `src/listing/listing.mutation.ts:417` |
| Mutation | `setActiveQueueEntry` | `UserFeedQueueMutationResolver.setActiveQueueEntry` | `Promise<boolean>` | `src/user-feed-queue/resolvers/user-feed-queue.mutation.ts:39` |
| Mutation | `setAddERC20PlatformFee` | `ListingMutation.setAddERC20PlatformFee` | `Promise<CustomMessageDTO>` | `src/listing/listing.mutation.ts:407` |
| Mutation | `setAssetFlagReviewed` | `ListingMutation.setAssetFlagReviewed` | `Promise<CustomMessageDTO>` | `src/listing/listing.mutation.ts:387` |
| Mutation | `setAssetUploaded` | `ListingMutation.setAssetUploaded` | `Promise<CustomMessageDTO>` | `src/listing/listing.mutation.ts:246` |
| Mutation | `setDownloadPrice` | `ListingMutation.setDownloadPrice` | `Promise<CustomMessageDTO>` | `src/listing/listing.mutation.ts:427` |
| Mutation | `setFreeDownload` | `ListingMutation.setFreeDownload` | `Promise<boolean>` | `src/listing/listing.mutation.ts:120` |
| Mutation | `setListingVisibility` | `ListingMutation.setListingVisibility` | `Promise<boolean>` | `src/listing/listing.mutation.ts:105` |
| Mutation | `setSourceFileAsThumbnail` | `ListingMutation.setSourceFileAsThumbnail` | `Promise<AssetDTO>` | `src/listing/listing.mutation.ts:232` |
| Mutation | `setupCreditTopUp` | `BillingMutation.setupCreditTopUp` | `Promise<CheckoutUrlDTO>` | `src/billing/billing.mutation.ts:142` |
| Mutation | `switchBillingInterval` | `BillingMutation.switchBillingInterval` | `Promise<CheckoutUrlDTO>` | `src/billing/billing.mutation.ts:113` |
| Mutation | `toggleFavorite` | `FolderMutation.toggleFavorite` | `Promise<boolean>` | `src/folder/resolvers/folder.mutation.ts:127` |
| Mutation | `toggleUserFavorite` | `ActivityMutation.toggleUserFavorite` | `Promise<CustomMessageDTO>` | `src/activity/activity.mutation.ts:59` |
| Mutation | `toggleUserFollow` | `ActivityMutation.toggleUserFollow` | `Promise<UserFollowDTO>` | `src/activity/activity.mutation.ts:48` |
| Mutation | `toggleUserLike` | `ActivityMutation.toggleUserLike` | `Promise<CustomMessageDTO>` | `src/activity/activity.mutation.ts:37` |
| Mutation | `unfollowFolder` | `FolderMutation.unfollowFolder` | `Promise<boolean>` | `src/folder/resolvers/folder.mutation.ts:187` |
| Mutation | `unlikeFolder` | `FolderMutation.unlikeFolder` | `Promise<boolean>` | `src/folder/resolvers/folder.mutation.ts:151` |
| Mutation | `unlinkAgent` | `UserMutation.unlinkAgent` | `Promise<boolean>` | `src/user/user.mutation.ts:119` |
| Mutation | `unpublishListing` | `ListingMutation.unpublishListing` | `Promise<CustomMessageDTO>` | `src/listing/listing.mutation.ts:93` |
| Mutation | `unsaveFolder` | `FolderMutation.unsaveFolder` | `Promise<boolean>` | `src/folder/resolvers/folder.mutation.ts:169` |
| Mutation | `updateAiModel` | `AiModelMutation.updateAiModel` | `Promise<AiModelResponseDTO>` | `src/ai-model/ai-model.mutation.ts:23` |
| Mutation | `updateConfigAmount` | `ConfigMutation.updateConfigAmount` | `Promise<Config>` | `src/config/config.mutation.ts:15` |
| Mutation | `updateCreatorStatus` | `UserMutation.updateCreatorStatus` | `Promise<CreatorStatus>` | `src/user/user.mutation.ts:260` |
| Mutation | `updateFolder` | `FolderMutation.updateFolder` | `Promise<Folder>` | `src/folder/resolvers/folder.mutation.ts:36` |
| Mutation | `updateListing` | `ListingMutation.updateListing` | `Promise<string>` | `src/listing/listing.mutation.ts:143` |
| Mutation | `updateListingPrice` | `ListingMutation.updateListingPrice` | `Promise<CustomMessageDTO>` | `src/listing/listing.mutation.ts:131` |
| Mutation | `updateNotificationSettingChannel` | `NotificationsMutation.updateNotificationSettingChannel` | `Promise<CustomMessageDTO>` | `src/notifications/notifications.mutation.ts:26` |
| Mutation | `updatePointAmount` | `PointMutation.updatePointAmount` | `Promise<PointType>` | `src/point/point.mutation.ts:28` |
| Mutation | `updateSocialMedia` | `UserMutation.updateSocialMedia` | `Promise<CreatorStatusDTO>` | `src/user/user.mutation.ts:228` |
| Mutation | `updateUserRole` | `UserMutation.updateUserRole` | `Promise<CustomMessageDTO>` | `src/user/user.mutation.ts:270` |
| Mutation | `updateUserStatus` | `UserMutation.updateUserStatus` | `Promise<UserStatus>` | `src/user/user.mutation.ts:250` |
| Mutation | `upgradeSubscription` | `BillingMutation.upgradeSubscription` | `Promise<CheckoutUrlDTO>` | `src/billing/billing.mutation.ts:60` |
| Mutation | `userAcceptPassword` | `UserMutation.userAcceptPassword` | `Promise<CustomMessageDTO>` | `src/user/user.mutation.ts:183` |
| Mutation | `userChangePassword` | `UserMutation.userChangePassword` | `Promise<CustomMessageDTO>` | `src/user/user.mutation.ts:194` |
| Mutation | `userCheck2faCode` | `UserMutation.userCheck2faCode` | `Promise<string>` | `src/user/user.mutation.ts:296` |
| Mutation | `userConfirmEmail` | `UserMutation.userConfirmEmail` | `Promise<CustomMessageDTO>` | `src/user/user.mutation.ts:150` |
| Mutation | `userFetchQrCode` | `UserMutation.userFetchQrCode` | `Promise<User2faCodeDTO>` | `src/user/user.mutation.ts:280` |
| Mutation | `userLogin` | `UserMutation.userLogin` | `Promise<UserLoginResponse>` | `src/user/user.mutation.ts:70` |
| Mutation | `userLogout` | `UserMutation.userLogout` | `Promise<boolean>` | `src/user/user.mutation.ts:99` |
| Mutation | `userResendVerificationEmail` | `UserMutation.userResendVerificationEmail` | `Promise<CustomMessageDTO>` | `src/user/user.mutation.ts:161` |
| Mutation | `userResetPassword` | `UserMutation.userResetPassword` | `Promise<CustomMessageDTO>` | `src/user/user.mutation.ts:172` |
| Mutation | `userSetUsername` | `UserMutation.userSetUsername` | `Promise<PrivateUser>` | `src/user/user.mutation.ts:219` |
| Mutation | `userSignup` | `UserMutation.userSignup` | `Promise<UserLoginResponse>` | `src/user/user.mutation.ts:57` |
| Mutation | `userUpdateAccount` | `UserMutation.userUpdateAccount` | `Promise<PrivateUser>` | `src/user/user.mutation.ts:208` |
| Mutation | `userUpdateNotificationSetting` | `UserMutation.userUpdateNotificationSetting` | `Promise<CustomMessageDTO>` | `src/user/user.mutation.ts:239` |
| Mutation | `userView` | `ActivityMutation.userView` | `Promise<CustomMessageDTO>` | `src/activity/activity.mutation.ts:70` |
| Mutation | `userWhitelistRequest` | `ActivityMutation.userWhitelistRequest` | `Promise<CustomMessageDTO>` | `src/activity/activity.mutation.ts:81` |
| Mutation | `validatePayPalCapture` | `PayPalMutation.validatePayPalCapture` | `Promise<boolean>` | `src/paypal/paypal.mutation.ts:92` |
| Mutation | `verifyMetamask` | `UserMutation.verifyMetamask` | `Promise<VerifyMetamaskResponseDTO>` | `src/user/user.mutation.ts:322` |
| Mutation | `verifyPayPalKYC` | `PayPalMutation.verifyPayPalKYC` | `Promise<PayPalOnboardingStatusDTO>` | `src/paypal/paypal.mutation.ts:40` |
| Mutation | `whitelistUser` | `ActivityMutation.whitelistUser` | `Promise<AdminUser>` | `src/activity/activity.mutation.ts:130` |
| Mutation | `whitelistUserByRequestId` | `ActivityMutation.whitelistUserByRequestId` | `Promise<CustomMessageDTO>` | `src/activity/activity.mutation.ts:140` |
| Query | `adminGetBillingSubscription` | `BillingAdminQuery.adminGetBillingSubscription` | `Promise<AdminBillingSubscriptionDTO>` | `src/billing/billing-admin.query.ts:10` |
| Query | `checkAssetsReady` | `ListingQuery.checkAssetsReady` | `Promise<AssetDTO[]>` | `src/listing/listing.query.ts:275` |
| Query | `checkAssetStatus` | `ListingQuery.checkAssetStatus` | `Promise<AssetStatusResponse>` | `src/listing/listing.query.ts:139` |
| Query | `checkIfWalletIsVerifiedByUser` | `UserQuery.checkIfWalletIsVerifiedByUser` | `Promise<WalletVerifiedResponseDTO>` | `src/user/user.query.ts:258` |
| Query | `checkUserLimit` | `UserQuery.checkUserLimit` | `Promise<UserLimitResponseDTO>` | `src/user/user.query.ts:306` |
| Query | `checkUsernameAvailable` | `UserQuery.checkUsernameAvailable` | `Promise<boolean>` | `src/user/user.query.ts:311` |
| Query | `communityExists` | `ListingQuery.communityExists` | `Promise<boolean>` | `src/listing/listing.query.ts:376` |
| Query | `fetchAllTiers` | `PermissionsQuery.fetchAllTiers` | `Promise<TierConfigDTO>` | `src/permissions/permissions.query.ts:10` |
| Query | `fetchCategories` | `ListingQuery.fetchCategories` | `Promise<Category[]>` | `src/listing/listing.query.ts:325` |
| Query | `fetchContractTypes` | `ListingQuery.fetchContractTypes` | `Promise<ContractType[]>` | `src/listing/listing.query.ts:341` |
| Query | `fetchFlaggedListings` | `SearchResolver.fetchFlaggedListings` | `Promise<ListingResponseWithTotalDTO>` | `src/search/search.resolver.ts:37` |
| Query | `fetchInitDraftListing` | `ListingQuery.fetchInitDraftListing` | `Promise<ListingDTO \| null>` | `src/listing/listing.query.ts:267` |
| Query | `fetchListingCount` | `ListingQuery.fetchListingCount` | `Promise<Number>` | `src/listing/listing.query.ts:311` |
| Query | `fetchListings` | `ListingQuery.fetchListings` | `Promise<ListingResponseWithTotalDTO>` | `src/listing/listing.query.ts:200` |
| Query | `fetchListingsByIds` | `ListingQuery.fetchListingsByIds` | `Promise<ListingDTO[]>` | `src/listing/listing.query.ts:228` |
| Query | `fetchListingsByUser` | `ListingQuery.fetchListingsByUser` | `Promise<PaginatedListingsDTO>` | `src/listing/listing.query.ts:242` |
| Query | `fetchListingsCursor` | `SearchResolver.fetchListingsCursor` | `Promise<PaginatedListings>` | `src/search/search.resolver.ts:138` |
| Query | `fetchListingStatus` | `ListingQuery.fetchListingStatus` | `Promise<ListingStatusResponseDTO>` | `src/listing/listing.query.ts:286` |
| Query | `fetchListingStatuses` | `ListingQuery.fetchListingStatuses` | `Promise<ListingStatus[]>` | `src/listing/listing.query.ts:334` |
| Query | `fetchPayToken` | `ListingQuery.fetchPayToken` | `Promise<PayToken>` | `src/listing/listing.query.ts:443` |
| Query | `fetchPayTokens` | `ListingQuery.fetchPayTokens` | `Promise<PayToken[]>` | `src/listing/listing.query.ts:451` |
| Query | `findAllUserNotifications` | `NotificationsQuery.findAllUserNotifications` | `Promise<NotificationReponseWithTotalDTO>` | `src/notifications/notifications.query.ts:15` |
| Query | `folder` | `FolderQuery.folder` | `Promise<Folder>` | `src/folder/resolvers/folder.query.ts:67` |
| Query | `folderListings` | `FolderQuery.folderListings` | `Promise<PaginatedFolderListings>` | `src/folder/resolvers/folder.query.ts:81` |
| Query | `getActiveAiModels` | `AiModelQuery.getActiveAiModels` | `Promise<AiModelResponseDTO[]>` | `src/ai-model/ai-model.query.ts:13` |
| Query | `getActivePurchaseSession` | `PayPalMutation.getActivePurchaseSession` | `Promise<BuyLinkDTO \| null>` | `src/paypal/paypal.mutation.ts:127` |
| Query | `getAddERC20PlatformFee` | `ListingQuery.getAddERC20PlatformFee` | `Promise<number>` | `src/listing/listing.query.ts:384` |
| Query | `getAdminComments` | `ActivityQuery.getAdminComments` | `Promise<CommentReponseWithTotalDTO>` | `src/activity/activity.query.ts:221` |
| Query | `getAgentPerformance` | `AnalyticsResolver.getAgentPerformance` | `Promise<AgentPerformanceDTO>` | `src/analytics/analytics.resolver.ts:168` |
| Query | `getAgentSuccessRate` | `AnalyticsResolver.getAgentSuccessRate` | `Promise<AgentSuccessRateDTO>` | `src/analytics/analytics.resolver.ts:176` |
| Query | `getAiModels` | `AiModelQuery.getAiModels` | `Promise<AiModelResponseDTO[]>` | `src/ai-model/ai-model.query.ts:18` |
| Query | `getAllPointEarned` | `PointQuery.getAllPointEarned` | `Promise<AllPointEarnedWithTotalDTO>` | `src/point/point.query.ts:34` |
| Query | `getAllUsers` | `UserQuery.getAllUsers` | `Promise<GetAllUsersReponseWithTotalDTO>` | `src/user/user.query.ts:198` |
| Query | `getAllUsersWithSocialMedia` | `UserQuery.getAllUsersWithSocialMedia` | `Promise<GetAllUsersReponseWithTotalDTO>` | `src/user/user.query.ts:208` |
| Query | `getAllWaitlist` | `UserQuery.getAllWaitlist` | `Promise<Waitlist[]>` | `src/user/user.query.ts:167` |
| Query | `getArtistViralListings` | `ListingQuery.getArtistViralListings` | `Promise<ListingDTO[]>` | `src/listing/listing.query.ts:157` |
| Query | `getAssetAccess` | `ListingQuery.getAssetAccess` | `Promise<AssetAccessResponse>` | `src/listing/listing.query.ts:148` |
| Query | `getAssetFlags` | `ListingQuery.getAssetFlags` | `Promise<AssetFlagResponseWithTotalDTO>` | `src/listing/listing.query.ts:392` |
| Query | `getBidsTotal` | `AuctionQuery.getBidsTotal` | `Promise<BidsTotalDTO>` | `src/auction/auction.query.ts:48` |
| Query | `getBidWars` | `AnalyticsResolver.getBidWars` | `Promise<TrendingListingsDTO>` | `src/analytics/analytics.resolver.ts:109` |
| Query | `getCategoryRanking` | `AnalyticsResolver.getCategoryRanking` | `Promise<CategoryStatsDTO[]>` | `src/analytics/analytics.resolver.ts:136` |
| Query | `getCategoryStats` | `AnalyticsResolver.getCategoryStats` | `Promise<CategoryStatsDTO>` | `src/analytics/analytics.resolver.ts:127` |
| Query | `getCommentFlags` | `ActivityQuery.getCommentFlags` | `Promise<CommentFlagDTO[]>` | `src/activity/activity.query.ts:231` |
| Query | `getConfigs` | `ConfigQuery.getConfigs` | `Promise<Config[]>` | `src/config/config.query.ts:24` |
| Query | `getCreatorAnalytics` | `AnalyticsResolver.getCreatorAnalytics` | `Promise<CreatorAnalyticsDTO>` | `src/analytics/analytics.resolver.ts:59` |
| Query | `getCreatorLeaderboard` | `AnalyticsResolver.getCreatorLeaderboard` | `Promise<LeaderboardDTO>` | `src/analytics/analytics.resolver.ts:148` |
| Query | `getCreatorTransactionHistory` | `AnalyticsResolver.getCreatorTransactionHistory` | `Promise<TransactionHistoryDTO>` | `src/analytics/analytics.resolver.ts:67` |
| Query | `getCreditBalance` | `BillingQuery.getCreditBalance` | `Promise<CreditBalanceDTO>` | `src/billing/billing.query.ts:76` |
| Query | `getCreditHistory` | `BillingQuery.getCreditHistory` | `Promise<CreditLedgerDTO[]>` | `src/billing/billing.query.ts:92` |
| Query | `getExportStatus` | `AnalyticsResolver.getExportStatus` | `Promise<BulkExportStatusDTO>` | `src/analytics/analytics.resolver.ts:196` |
| Query | `getFAQs` | `UserQuery.getFAQs` | `Promise<QA[]>` | `src/user/user.query.ts:284` |
| Query | `getFAQsAdmin` | `UserQuery.getFAQsAdmin` | `Promise<QA[]>` | `src/user/user.query.ts:295` |
| Query | `getFeatureFlags` | `ConfigQuery.getFeatureFlags` | `Promise<FeatureFlagsDTO>` | `src/config/config.query.ts:31` |
| Query | `getFeed` | `FeedResolver.getFeed` | `Promise<FeedResponseDTO>` | `src/feed/feed.resolver.ts:10` |
| Query | `getFinalizedPayTokens` | `ListingQuery.getFinalizedPayTokens` | `Promise<PayTokenResponseWithTotalDTO>` | `src/listing/listing.query.ts:434` |
| Query | `getHotListings` | `AnalyticsResolver.getHotListings` | `Promise<TrendingListingsDTO>` | `src/analytics/analytics.resolver.ts:83` |
| Query | `getListing` | `ListingQuery.getListing` | `Promise<ListingDTO>` | `src/listing/listing.query.ts:115` |
| Query | `getListingActivity` | `ActivityQuery.getListingActivity` | `Promise<ListingActivityDTO>` | `src/activity/activity.query.ts:135` |
| Query | `getListingAnalytics` | `AnalyticsResolver.getListingAnalytics` | `Promise<ListingAnalyticsDTO>` | `src/analytics/analytics.resolver.ts:28` |
| Query | `getListingBid` | `AuctionQuery.getListingBid` | `Promise<BidDTO>` | `src/auction/auction.query.ts:26` |
| Query | `getListingByName` | `ListingQuery.getListingByName` | `Promise<ListingDTO>` | `src/listing/listing.query.ts:79` |
| Query | `getListingBySlug` | `ListingQuery.getListingBySlug` | `Promise<ListingDTO>` | `src/listing/listing.query.ts:97` |
| Query | `getListingComments` | `ActivityQuery.getListingComments` | `Promise<CommentReponseWithTotalDTO>` | `src/activity/activity.query.ts:192` |
| Query | `getListingCommentsCursor` | `ActivityQuery.getListingCommentsCursor` | `Promise<PaginatedComments>` | `src/activity/activity.query.ts:203` |
| Query | `getListingFile` | `ListingQuery.getListingFile` | `Promise<ListingFileResponseDTO[]>` | `src/listing/listing.query.ts:186` |
| Query | `getListingFlags` | `ListingQuery.getListingFlags` | `Promise<ListingFlagDTO[]>` | `src/listing/listing.query.ts:348` |
| Query | `getListingLikes` | `ActivityQuery.getListingLikes` | `Promise<number>` | `src/activity/activity.query.ts:39` |
| Query | `getListingMetadata` | `ListingQuery.getListingMetadata` | `Promise<ListingMetadataDTO>` | `src/listing/listing.query.ts:168` |
| Query | `getListingOffers` | `MarketplaceQuery.getListingOffers` | `Promise<OfferDTO[]>` | `src/marketplace/marketplace.query.ts:41` |
| Query | `getListingPriceHistory` | `AnalyticsResolver.getListingPriceHistory` | `Promise<PriceHistoryDTO>` | `src/analytics/analytics.resolver.ts:36` |
| Query | `getListingProcessLogs` | `ListingQuery.getListingProcessLogs` | `Promise<ListingProcessLog[]>` | `src/listing/listing.query.ts:358` |
| Query | `getListingRank` | `ViralScoreQuery.getListingRank` | `Promise<number>` | `src/viral-score/viral-score.query.ts:21` |
| Query | `getListings` | `ListingQuery.getListings` | `Promise<ListingDTO[]>` | `src/listing/listing.query.ts:130` |
| Query | `getListingTradeHistories` | `ActivityQuery.getListingTradeHistories` | `Promise<TradeHistoryDTO[]>` | `src/activity/activity.query.ts:122` |
| Query | `getListingTransactionHistory` | `AnalyticsResolver.getListingTransactionHistory` | `Promise<TransactionHistoryDTO>` | `src/analytics/analytics.resolver.ts:45` |
| Query | `getListingViewCount` | `ActivityQuery.getListingViewCount` | `Promise<number>` | `src/activity/activity.query.ts:69` |
| Query | `getMentions` | `MentionQuery.getMentions` | `Promise<MentionDTO[]>` | `src/mention/mention.query.ts:13` |
| Query | `getMonthlyTotalPointEarned` | `PointQuery.getMonthlyTotalPointEarned` | `Promise<number>` | `src/point/point.query.ts:44` |
| Query | `getMyDownloadLicenses` | `ListingQuery.getMyDownloadLicenses` | `Promise<Transaction[]>` | `src/listing/listing.query.ts:259` |
| Query | `getMyInteractionsTotal` | `ActivityQuery.getMyInteractionsTotal` | `Promise<InteractionsTotalDTO>` | `src/activity/activity.query.ts:182` |
| Query | `getMySingleItemsTotal` | `ListingQuery.getMySingleItemsTotal` | `Promise<Number>` | `src/listing/listing.query.ts:211` |
| Query | `getNewSellers` | `AnalyticsResolver.getNewSellers` | `Promise<LeaderboardEntryDTO[]>` | `src/analytics/analytics.resolver.ts:117` |
| Query | `getNotificationsCursor` | `NotificationsQuery.getNotificationsCursor` | `Promise<PaginatedNotifications>` | `src/notifications/notifications.query.ts:29` |
| Query | `getOffersTotal` | `MarketplaceQuery.getOffersTotal` | `Promise<OffersTotalDTO>` | `src/marketplace/marketplace.query.ts:55` |
| Query | `getOutboxEntries` | `OutboxResolver.getOutboxEntries` | `Promise<OutboxEntryDTO[]>` | `src/resilience/outbox/outbox.resolver.ts:10` |
| Query | `getPayTokens` | `ListingQuery.getPayTokens` | `Promise<PayTokenResponseWithTotalDTO>` | `src/listing/listing.query.ts:413` |
| Query | `getPendingFiles` | `ListingQuery.getPendingFiles` | `Promise<AssetDTO[]>` | `src/listing/listing.query.ts:368` |
| Query | `getPendingTransaction` | `ListingQuery.getPendingTransaction` | `Promise<Transaction>` | `src/listing/listing.query.ts:300` |
| Query | `getPlacedBids` | `AuctionQuery.getPlacedBids` | `Promise<BidsResponseDTO>` | `src/auction/auction.query.ts:37` |
| Query | `getPlans` | `BillingQuery.getPlans` | `Promise<PlanDTO[]>` | `src/billing/billing.query.ts:103` |
| Query | `getPointsBalance` | `PointQuery.getPointsBalance` | `Promise<PointsBalanceDTO>` | `src/point/point.query.ts:54` |
| Query | `getPointTypes` | `PointQuery.getPointTypes` | `Promise<PointType[]>` | `src/point/point.query.ts:17` |
| Query | `getPriceMovers` | `AnalyticsResolver.getPriceMovers` | `Promise<TrendingListingsDTO>` | `src/analytics/analytics.resolver.ts:100` |
| Query | `getProfileCounts` | `UserQuery.getProfileCounts` | `Promise<ProfileCountsDTO>` | `src/user/user.query.ts:96` |
| Query | `getProfileDashboard` | `UserQuery.getProfileDashboard` | `Promise<ProfileDashboardDTO>` | `src/user/user.query.ts:104` |
| Query | `getPurchaseStatus` | `ListingQuery.getPurchaseStatus` | `Promise<PurchaseStatusDTO>` | `src/listing/listing.query.ts:474` |
| Query | `getQuestionTypes` | `UserQuery.getQuestionTypes` | `Promise<QuestionType[]>` | `src/user/user.query.ts:301` |
| Query | `getReceivedBids` | `AuctionQuery.getReceivedBids` | `Promise<BidsResponseDTO>` | `src/auction/auction.query.ts:15` |
| Query | `getReceivedOffers` | `MarketplaceQuery.getReceivedOffers` | `Promise<OffersResponseDTO>` | `src/marketplace/marketplace.query.ts:16` |
| Query | `getRepeatBuyerRate` | `AnalyticsResolver.getRepeatBuyerRate` | `Promise<RepeatBuyerRateDTO>` | `src/analytics/analytics.resolver.ts:158` |
| Query | `getRewardTokenInfor` | `UserQuery.getRewardTokenInfor` | `Promise<RewardTokenInforDTO>` | `src/user/user.query.ts:289` |
| Query | `getRewardTradeHistories` | `PointQuery.getRewardTradeHistories` | `Promise<PointResponseDTO>` | `src/point/point.query.ts:23` |
| Query | `getSentOffers` | `MarketplaceQuery.getSentOffers` | `Promise<OffersResponseDTO>` | `src/marketplace/marketplace.query.ts:30` |
| Query | `getSingleAssetFlag` | `ListingQuery.getSingleAssetFlag` | `Promise<AssetFlagDTO>` | `src/listing/listing.query.ts:402` |
| Query | `getSingleUser` | `UserQuery.getSingleUser` | `Promise<AdminUser>` | `src/user/user.query.ts:218` |
| Query | `getSubscription` | `BillingQuery.getSubscription` | `Promise<SubscriptionDTO>` | `src/billing/billing.query.ts:26` |
| Query | `getTierPricing` | `BillingQuery.getTierPricing` | `Promise<TierPriceDTO[]>` | `src/billing/billing.query.ts:173` |
| Query | `getTopUpTiers` | `BillingQuery.getTopUpTiers` | `Promise<TopUpTierDTO[]>` | `src/billing/billing.query.ts:163` |
| Query | `getTotalShare` | `ActivityQuery.getTotalShare` | `Promise<Number>` | `src/activity/activity.query.ts:155` |
| Query | `getTransferSignature` | `ActivityQuery.getTransferSignature` | `Promise<string>` | `src/activity/activity.query.ts:162` |
| Query | `getTrendingListings` | `AnalyticsResolver.getTrendingListings` | `Promise<TrendingListingsDTO>` | `src/analytics/analytics.resolver.ts:91` |
| Query | `getUserAccountDetails` | `UserQuery.getUserAccountDetails` | `Promise<PrivateUser>` | `src/user/user.query.ts:153` |
| Query | `getUserFollowerAccounts` | `ActivityQuery.getUserFollowerAccounts` | `Promise<PublicUser[]>` | `src/activity/activity.query.ts:94` |
| Query | `getUserFollowingAccounts` | `ActivityQuery.getUserFollowingAccounts` | `Promise<PublicUser[]>` | `src/activity/activity.query.ts:108` |
| Query | `getUserGrandReferrals` | `UserQuery.getUserGrandReferrals` | `Promise<ReferralDTO[]>` | `src/user/user.query.ts:76` |
| Query | `getUserInteractionsForListings` | `SearchResolver.getUserInteractionsForListings` | `Promise<ListingInteractionDTO[]>` | `src/search/search.resolver.ts:147` |
| Query | `getUserInteractionsTotal` | `ActivityQuery.getUserInteractionsTotal` | `Promise<InteractionsTotalDTO>` | `src/activity/activity.query.ts:173` |
| Query | `getUserInviteTokens` | `UserQuery.getUserInviteTokens` | `Promise<RegistrationToken[]>` | `src/user/user.query.ts:183` |
| Query | `getUserNetworkInfo` | `ActivityQuery.getUserNetworkInfo` | `Promise<UserNetworkDTO>` | `src/activity/activity.query.ts:76` |
| Query | `getUserNetworkInfoById` | `ActivityQuery.getUserNetworkInfoById` | `Promise<UserNetworkDTO>` | `src/activity/activity.query.ts:85` |
| Query | `getUserNotificationSettings` | `UserQuery.getUserNotificationSettings` | `Promise<NotificationSetting[]>` | `src/user/user.query.ts:244` |
| Query | `getUserPayTokens` | `ListingQuery.getUserPayTokens` | `Promise<PayTokenResponseWithTotalDTO>` | `src/listing/listing.query.ts:422` |
| Query | `getUserPayTokensTotal` | `ListingQuery.getUserPayTokensTotal` | `Promise<number>` | `src/listing/listing.query.ts:466` |
| Query | `getUserProfile` | `UserQuery.getUserProfile` | `Promise<PrivateUser>` | `src/user/user.query.ts:42` |
| Query | `getUserProfileByUserName` | `UserQuery.getUserProfileByUserName` | `Promise<PublicUser>` | `src/user/user.query.ts:235` |
| Query | `getUserProfileByWalletAddress` | `UserQuery.getUserProfileByWalletAddress` | `Promise<PublicUser>` | `src/user/user.query.ts:226` |
| Query | `getUserReferralCode` | `UserQuery.getUserReferralCode` | `Promise<ReferralResponseDTO>` | `src/user/user.query.ts:66` |
| Query | `getUserReferrals` | `UserQuery.getUserReferrals` | `Promise<ReferralDTO[]>` | `src/user/user.query.ts:54` |
| Query | `getUserReferralsTotal` | `UserQuery.getUserReferralsTotal` | `Promise<number>` | `src/user/user.query.ts:90` |
| Query | `getUserSingleItemsTotal` | `ListingQuery.getUserSingleItemsTotal` | `Promise<Number>` | `src/listing/listing.query.ts:219` |
| Query | `getUserViralScore` | `ViralScoreQuery.getUserViralScore` | `Promise<number>` | `src/viral-score/viral-score.query.ts:28` |
| Query | `getUserWaitlist` | `UserQuery.getUserWaitlist` | `Promise<Waitlist[]>` | `src/user/user.query.ts:175` |
| Query | `getValidationString` | `UserQuery.getValidationString` | `Promise<ValidationStringResponseDTO>` | `src/user/user.query.ts:275` |
| Query | `getViralScore` | `ViralScoreQuery.getViralScore` | `Promise<number \| null>` | `src/viral-score/viral-score.query.ts:13` |
| Query | `isUserFollowing` | `ActivityQuery.isUserFollowing` | `Promise<boolean>` | `src/activity/activity.query.ts:58` |
| Query | `listingFolders` | `FolderQuery.listingFolders` | `Promise<Folder[]>` | `src/folder/resolvers/folder.query.ts:132` |
| Query | `myFeedHistory` | `UserFeedQueueQueryResolver.myFeedHistory` | `Promise<UserFeedHistoryPageDto>` | `src/user-feed-queue/resolvers/user-feed-queue.query.ts:22` |
| Query | `myFeedQueue` | `UserFeedQueueQueryResolver.myFeedQueue` | `Promise<UserFeedQueueDto>` | `src/user-feed-queue/resolvers/user-feed-queue.query.ts:14` |
| Query | `myFolderEngagement` | `FolderQuery.myFolderEngagement` | `Promise<FolderEngagementState>` | `src/folder/resolvers/folder.query.ts:151` |
| Query | `myFolders` | `FolderQuery.myFolders` | `Promise<Folder[]>` | `src/folder/resolvers/folder.query.ts:47` |
| Query | `mySavedFolders` | `FolderQuery.mySavedFolders` | `Promise<Folder[]>` | `src/folder/resolvers/folder.query.ts:57` |
| Query | `ownerPublicFolders` | `FolderQuery.ownerPublicFolders` | `Promise<Folder[]>` | `src/folder/resolvers/folder.query.ts:123` |
| Query | `ownerPublicPlaylists` | `FolderQuery.ownerPublicPlaylists` | `Promise<Folder[]>` | `src/folder/resolvers/folder.query.ts:114` |
| Query | `ownerPublicPortfolios` | `FolderQuery.ownerPublicPortfolios` | `Promise<Folder[]>` | `src/folder/resolvers/folder.query.ts:105` |
| Query | `payTokenExists` | `ListingQuery.payTokenExists` | `Promise<boolean>` | `src/listing/listing.query.ts:458` |
| Query | `previewListingVisibilityChange` | `ListingQuery.previewListingVisibilityChange` | `Promise<VisibilityChangePreviewDTO>` | `src/listing/listing.query.ts:483` |
| Query | `searchFolders` | `SearchResolver.searchFolders` | `Promise<PaginatedFoldersSearchResult>` | `src/search/search.resolver.ts:172` |
| Query | `searchNames` | `ListingQuery.searchNames` | `Promise<SearchNamesResponseDTO>` | `src/listing/listing.query.ts:70` |
| Query | `searchUsers` | `SearchResolver.searchUsers` | `Promise<PublicUser[]>` | `src/search/search.resolver.ts:159` |
| Query | `sendReferralEmail` | `UserQuery.sendReferralEmail` | `Promise<boolean>` | `src/user/user.query.ts:142` |
| Query | `validateInviteCode` | `UserQuery.validateInviteCode` | `Promise<boolean>` | `src/user/user.query.ts:193` |

## Details

### Mutation acceptCounterOffer

- Source: `src/marketplace/marketplace.mutation.ts:83`
- Handler: `MarketplaceMutation.acceptCounterOffer`
- Declared return: `Promise<CustomMessageDTO>`
- Decorators: `@Authorize('user')`, `@Mutation(() => CustomMessageDTO)`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @Args | `offerId` | `string` | `'offerId'` |
| @GetUserId | `userId` | `string` | `` |

### Mutation acceptOffer

- Source: `src/marketplace/marketplace.mutation.ts:50`
- Handler: `MarketplaceMutation.acceptOffer`
- Declared return: `Promise<CustomMessageDTO>`
- Decorators: `@Authorize('user')`, `@Mutation(() => CustomMessageDTO)`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @Args | `input` | `InputUUID` | `'input'` |
| @GetUserId | `userId` | `string` | `` |

### Mutation addComment

- Source: `src/activity/activity.mutation.ts:170`
- Handler: `ActivityMutation.addComment`
- Declared return: `Promise<CommentDTO>`
- Decorators: `@Throttle({ default: { limit: 5, ttl: 60000 } })`, `@Authorize('user')`, `@Mutation(() => CommentDTO)`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @Args | `input` | `AddCommentDTO` | `'input'` |
| @GetUserId | `userId` | `string` | `` |

### Mutation addCommentFlag

- Source: `src/activity/activity.mutation.ts:204`
- Handler: `ActivityMutation.addCommentFlag`
- Declared return: `Promise<CustomMessageDTO>`
- Decorators: `@Throttle({ default: { limit: 5, ttl: 60000 } })`, `@Authorize('user')`, `@Mutation(() => CustomMessageDTO)`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @Args | `input` | `AddCommentFlagDTO` | `'input'` |
| @GetUserId | `userId` | `string` | `` |

### Mutation addCommentVote

- Source: `src/activity/activity.mutation.ts:193`
- Handler: `ActivityMutation.addCommentVote`
- Declared return: `Promise<CommentVote>`
- Decorators: `@Authorize('user')`, `@Mutation(() => CommentVote, { nullable: true })`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @Args | `input` | `AddCommentVoteDTO` | `'input'` |
| @GetUserId | `userId` | `string` | `` |

### Mutation addListingFlag

- Source: `src/listing/listing.mutation.ts:345`
- Handler: `ListingMutation.addListingFlag`
- Declared return: `Promise<CustomMessageDTO>`
- Decorators: `@Throttle({ default: { limit: 5, ttl: 60000 } })`, `@Authorize('user')`, `@Mutation(() => CustomMessageDTO)`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @Args | `input` | `AddListingFlagDTO` | `'input'` |
| @GetUserId | `userId` | `string` | `` |

### Mutation addOrUpdateCategory

- Source: `src/listing/listing.mutation.ts:325`
- Handler: `ListingMutation.addOrUpdateCategory`
- Declared return: `Promise<Category>`
- Decorators: `@Authorize('admin')`, `@Mutation(() => Category)`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @Args | `input` | `CreateCategoryDTO` | `'input'` |

### Mutation addOrUpdateQA

- Source: `src/user/user.mutation.ts:347`
- Handler: `UserMutation.addOrUpdateQA`
- Declared return: `Promise<QA>`
- Decorators: `@Authorize('admin')`, `@Mutation(() => QA)`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @Args | `input` | `CreateQADTO` | `'input'` |

### Mutation addOrUpdateQuestionType

- Source: `src/user/user.mutation.ts:363`
- Handler: `UserMutation.addOrUpdateQuestionType`
- Declared return: `Promise<QuestionType>`
- Decorators: `@Authorize('admin')`, `@Mutation(() => QuestionType)`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @Args | `input` | `CreateQuestionTypeDTO` | `'input'` |

### Mutation addPayToken

- Source: `src/listing/listing.mutation.ts:278`
- Handler: `ListingMutation.addPayToken`
- Declared return: `Promise<CustomMessageDTO>`
- Decorators: `@Authorize('user')`, `@Mutation(() => CustomMessageDTO)`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @Args | `input` | `CreatePayTokenDTO` | `'input'` |
| @GetUserId | `userId` | `string` | `` |

### Mutation addPointType

- Source: `src/point/point.mutation.ts:14`
- Handler: `PointMutation.addPointType`
- Declared return: `Promise<PointType>`
- Decorators: `@Authorize('admin')`, `@Mutation(() => PointType)`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @Args | `input` | `PointTypeDTO` | `'input'` |

### Mutation addToWaitlist

- Source: `src/user/user.mutation.ts:126`
- Handler: `UserMutation.addToWaitlist`
- Declared return: `Promise<CustomMessageDTO>`
- Decorators: `@Throttle({ default: { limit: 5, ttl: 60000 } })`, `@Mutation(() => CustomMessageDTO)`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @Args | `input` | `AddToWaitlistDTO` | `'input'` |

### Mutation addTransaction

- Source: `src/listing/listing.mutation.ts:174`
- Handler: `ListingMutation.addTransaction`
- Declared return: `Promise<CustomMessageDTO>`
- Decorators: `@Authorize('user')`, `@Mutation(() => CustomMessageDTO)`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @Args | `input` | `TransactionDTO` | `'input'` |
| @GetUserId | `userId` | `string` | `` |

### Mutation adminApproveWaitlist

- Source: `src/user/user.mutation.ts:393`
- Handler: `UserMutation.adminApproveWaitlist`
- Declared return: `Promise<CustomMessageDTO>`
- Decorators: `@Authorize('admin')`, `@Mutation(() => CustomMessageDTO)`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @Args | `input` | `AdminApproveWaitlistDTO` | `'input'` |

### Mutation adminApproveWaitlists

- Source: `src/user/user.mutation.ts:402`
- Handler: `UserMutation.adminApproveWaitlists`
- Declared return: `Promise<CustomMessageDTO>`
- Decorators: `@Authorize('admin')`, `@Mutation(() => CustomMessageDTO)`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @Args | `input` | `AdminApproveWaitlistsDTO` | `'input'` |

### Mutation adminCancelSubscription

- Source: `src/billing/billing-admin.mutation.ts:21`
- Handler: `BillingAdminMutation.adminCancelSubscription`
- Declared return: `Promise<boolean>`
- Decorators: `@Authorize('admin')`, `@Mutation(() => Boolean)`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @Args | `input` | `AdminCancelSubscriptionDTO` | `'input'` |

### Mutation adminGrantSubscription

- Source: `src/billing/billing-admin.mutation.ts:13`
- Handler: `BillingAdminMutation.adminGrantSubscription`
- Declared return: `Promise<boolean>`
- Decorators: `@Authorize('admin')`, `@Mutation(() => Boolean)`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @Args | `input` | `AdminGrantSubscriptionDTO` | `'input'` |

### Mutation adminLogin

- Source: `src/user/user.mutation.ts:138`
- Handler: `UserMutation.adminLogin`
- Declared return: `Promise<AdminLoginResponse>`
- Decorators: `@Mutation(() => AdminLoginResponse)`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @Args | `input` | `AdminLoginDTO` | `'input'` |

### Mutation approveListing

- Source: `src/listing/listing.mutation.ts:156`
- Handler: `ListingMutation.approveListing`
- Declared return: `Promise<ListingDTO>`
- Decorators: `@Authorize('admin')`, `@Mutation(() => ListingDTO)`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @Args | `input` | `InputUUID` | `'input'` |

### Mutation authorizePayPalPayment

- Source: `src/paypal/paypal.mutation.ts:75`
- Handler: `PayPalMutation.authorizePayPalPayment`
- Declared return: `Promise<string>`
- Decorators: `@UseGuards(MarketplaceEnabledGuard)`, `@Authorize('user')`, `@Mutation(() => String)`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @Args | `input` | `AuthorizePayPalPaymentDTO` | `'input'` |
| @GetUserId | `userId` | `string` | `` |

### Mutation backfillSearchIndex

- Source: `src/search/search.resolver.ts:180`
- Handler: `SearchResolver.backfillSearchIndex`
- Declared return: `Promise<boolean>`
- Decorators: `@Authorize('admin')`, `@Mutation(() => Boolean)`

Arguments/context bindings:

_None declared._

### Mutation bulkAddListingsToFolder

- Source: `src/folder/resolvers/folder.mutation.ts:198`
- Handler: `FolderMutation.bulkAddListingsToFolder`
- Declared return: `Promise<BulkAddResultType>`
- Decorators: `@Mutation(() => BulkAddResultType)`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @GetUserId | `userId` | `string` | `` |
| @Args | `folderId` | `string` | `'folderId', new ParseUUIDPipe()` |
| @Args | `input` | `BulkAddListingsInput` | `'input'` |

### Mutation bulkRemoveListingsFromFolder

- Source: `src/folder/resolvers/folder.mutation.ts:207`
- Handler: `FolderMutation.bulkRemoveListingsFromFolder`
- Declared return: `Promise<BulkRemoveResultType>`
- Decorators: `@Mutation(() => BulkRemoveResultType)`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @GetUserId | `userId` | `string` | `` |
| @Args | `folderId` | `string` | `'folderId', new ParseUUIDPipe()` |
| @Args | `input` | `BulkRemoveListingsInput` | `'input'` |

### Mutation calcPayPalEstimate

- Source: `src/paypal/paypal.mutation.ts:106`
- Handler: `PayPalMutation.calcPayPalEstimate`
- Declared return: `Promise<number>`
- Decorators: `@UseGuards(MarketplaceEnabledGuard)`, `@Authorize('user')`, `@Mutation(() => Number)`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @Args | `input` | `InputPayPalEstimateDTO` | `'input'` |

### Mutation cancelBuyAsset

- Source: `src/marketplace/marketplace.mutation.ts:63`
- Handler: `MarketplaceMutation.cancelBuyAsset`
- Declared return: `Promise<CustomMessageDTO>`
- Decorators: `@Authorize('user')`, `@Mutation(() => CustomMessageDTO)`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @Args | `input` | `InputUUID` | `'input'` |
| @GetUserId | `userId` | `string` | `` |

### Mutation cancelCreditTopUp

- Source: `src/billing/billing.mutation.ts:164`
- Handler: `BillingMutation.cancelCreditTopUp`
- Declared return: `Promise<boolean>`
- Decorators: `@Mutation(() => Boolean)`, `@Authorize('user')`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @GetUserId | `userId` | `string` | `` |

### Mutation cancelOffer

- Source: `src/marketplace/marketplace.mutation.ts:37`
- Handler: `MarketplaceMutation.cancelOffer`
- Declared return: `Promise<CustomMessageDTO>`
- Decorators: `@Authorize('user')`, `@Mutation(() => CustomMessageDTO)`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @Args | `listingId` | `string` | `'input'` |
| @GetUserId | `userId` | `string` | `` |

### Mutation cancelPendingDowngrade

- Source: `src/billing/billing.mutation.ts:136`
- Handler: `BillingMutation.cancelPendingDowngrade`
- Declared return: `Promise<boolean>`
- Decorators: `@Mutation(() => Boolean)`, `@Authorize('user')`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @GetUserId | `userId` | `string` | `` |

### Mutation cancelSubscription

- Source: `src/billing/billing.mutation.ts:54`
- Handler: `BillingMutation.cancelSubscription`
- Declared return: `Promise<boolean>`
- Decorators: `@Mutation(() => Boolean)`, `@Authorize('user')`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @GetUserId | `userId` | `string` | `` |

### Mutation clearFeedHistory

- Source: `src/user-feed-queue/resolvers/user-feed-queue.mutation.ts:60`
- Handler: `UserFeedQueueMutationResolver.clearFeedHistory`
- Declared return: `Promise<number>`
- Decorators: `@Mutation(() => Int)`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @GetUserId | `userId` | `string` | `` |

### Mutation clearQueue

- Source: `src/user-feed-queue/resolvers/user-feed-queue.mutation.ts:47`
- Handler: `UserFeedQueueMutationResolver.clearQueue`
- Declared return: `Promise<number>`
- Decorators: `@Mutation(() => Int)`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @GetUserId | `userId` | `string` | `` |

### Mutation confirmOwnershipPurchase

- Source: `src/paypal/paypal.mutation.ts:137`
- Handler: `PayPalMutation.confirmOwnershipPurchase`
- Declared return: `Promise<ConfirmOwnershipPurchaseResponseDTO>`
- Decorators: `@UseGuards(MarketplaceEnabledGuard)`, `@Authorize('user')`, `@Mutation(() => ConfirmOwnershipPurchaseResponseDTO)`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @Args | `input` | `ConfirmOwnershipPurchaseDTO` | `'input'` |
| @GetUserId | `userId` | `string` | `` |

### Mutation copyShareLink

- Source: `src/activity/activity.mutation.ts:118`
- Handler: `ActivityMutation.copyShareLink`
- Declared return: `Promise<CustomMessageDTO>`
- Decorators: `@Throttle({ default: { limit: 20, ttl: 60000 } })`, `@Authorize('user')`, `@Mutation(() => CustomMessageDTO)`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @Args | `input` | `InputUUID` | `'input'` |
| @GetUserId | `userId` | `string` | `` |

### Mutation counterOffer

- Source: `src/marketplace/marketplace.mutation.ts:74`
- Handler: `MarketplaceMutation.counterOffer`
- Declared return: `Promise<OfferDTO>`
- Decorators: `@Authorize('user')`, `@Mutation(() => OfferDTO)`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @Args | `input` | `CounterOfferInputDTO` | `'input'` |
| @GetUserId | `userId` | `string` | `` |

### Mutation createAiModel

- Source: `src/ai-model/ai-model.mutation.ts:15`
- Handler: `AiModelMutation.createAiModel`
- Declared return: `Promise<AiModelResponseDTO>`
- Decorators: `@Authorize('admin')`, `@Mutation(() => AiModelResponseDTO)`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @Args | `input` | `CreateAiModelDTO` | `'input'` |

### Mutation createBillingPortalSession

- Source: `src/billing/billing.mutation.ts:180`
- Handler: `BillingMutation.createBillingPortalSession`
- Declared return: `Promise<CheckoutUrlDTO>`
- Decorators: `@Mutation(() => CheckoutUrlDTO)`, `@Authorize('user')`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @GetUserId | `userId` | `string` | `` |

### Mutation createFolder

- Source: `src/folder/resolvers/folder.mutation.ts:28`
- Handler: `FolderMutation.createFolder`
- Declared return: `Promise<Folder>`
- Decorators: `@Mutation(() => Folder)`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @GetUserId | `userId` | `string` | `` |
| @Args | `input` | `CreateFolderInput` | `'input'` |

### Mutation createOwnershipAuthorizeLink

- Source: `src/paypal/paypal.mutation.ts:117`
- Handler: `PayPalMutation.createOwnershipAuthorizeLink`
- Declared return: `Promise<BuyLinkDTO>`
- Decorators: `@UseGuards(MarketplaceEnabledGuard)`, `@Authorize('user')`, `@Mutation(() => BuyLinkDTO)`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @Args | `input` | `InputUUID` | `'input'` |
| @GetUserId | `userId` | `string` | `` |

### Mutation createPaymentMethodUpdateFlow

- Source: `src/billing/billing.mutation.ts:170`
- Handler: `BillingMutation.createPaymentMethodUpdateFlow`
- Declared return: `Promise<CheckoutUrlDTO>`
- Decorators: `@Mutation(() => CheckoutUrlDTO)`, `@Authorize('user')`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @GetUserId | `userId` | `string` | `` |

### Mutation createPayPalBuyLink

- Source: `src/paypal/paypal.mutation.ts:49`
- Handler: `PayPalMutation.createPayPalBuyLink`
- Declared return: `Promise<BuyLinkDTO>`
- Decorators: `@UseGuards(MarketplaceEnabledGuard)`, `@Authorize('user')`, `@Mutation(() => BuyLinkDTO)`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @Args | `input` | `InputUUID` | `'input'` |
| @GetUserId | `userId` | `string` | `` |

### Mutation createPayPalDownloadLicenseLink

- Source: `src/paypal/paypal.mutation.ts:61`
- Handler: `PayPalMutation.createPayPalDownloadLicenseLink`
- Declared return: `Promise<BuyLinkDTO>`
- Decorators: `@UseGuards(MarketplaceEnabledGuard)`, `@Authorize('user')`, `@Mutation(() => BuyLinkDTO)`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @Args | `input` | `InputUUID` | `'input'` |
| @GetUserId | `userId` | `string` | `` |

### Mutation createShare

- Source: `src/activity/activity.mutation.ts:92`
- Handler: `ActivityMutation.createShare`
- Declared return: `Promise<string>`
- Decorators: `@Authorize('user')`, `@Mutation(() => String)`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @Args | `sourceId` | `string` | `'source_id'` |
| @GetUserId | `userId` | `string` | `` |

### Mutation createSubscriptionCheckout

- Source: `src/billing/billing.mutation.ts:17`
- Handler: `BillingMutation.createSubscriptionCheckout`
- Declared return: `Promise<CheckoutUrlDTO>`
- Decorators: `@Mutation(() => CheckoutUrlDTO)`, `@Authorize('user')`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @GetUserId | `userId` | `string` | `` |
| @GetUserEmail | `email` | `string` | `` |
| @Args | `plan` | `string` | `'plan', { type: () => String, nullable: false }` |
| @Args | `interval` | `string` | `'interval', { type: () => String, defaultValue: 'monthly' }` |

### Mutation createUploadPresignedUrl

- Source: `src/listing/listing.mutation.ts:206`
- Handler: `ListingMutation.createUploadPresignedUrl`
- Declared return: `Promise<CreateUploadPresignedUrlResponseDTO>`
- Decorators: `@Authorize('user')`, `@Throttle({ default: { limit: 5, ttl: 60000 } })`, `@Mutation(() => CreateUploadPresignedUrlResponseDTO)`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @Args | `input` | `CreateUploadPresignedUrlDTO` | `'input'` |
| @GetUserId | `userId` | `string` | `` |

### Mutation createUserPresignedUrl

- Source: `src/user/user.mutation.ts:336`
- Handler: `UserMutation.createUserPresignedUrl`
- Declared return: `Promise<CreateUserPresignedUrlResponseDTO>`
- Decorators: `@Authorize('user')`, `@Mutation(() => CreateUserPresignedUrlResponseDTO)`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @Args | `input` | `CreateUserPresignedUrlDTO` | `'input'` |
| @GetUserId | `userId` | `string` | `` |

### Mutation deleteAiModel

- Source: `src/ai-model/ai-model.mutation.ts:31`
- Handler: `AiModelMutation.deleteAiModel`
- Declared return: `Promise<boolean>`
- Decorators: `@Authorize('admin')`, `@Mutation(() => Boolean)`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @Args | `aiModelId` | `number` | `'aiModelId', { type: () => Int }` |

### Mutation deleteAssetFlag

- Source: `src/listing/listing.mutation.ts:397`
- Handler: `ListingMutation.deleteAssetFlag`
- Declared return: `Promise<CustomMessageDTO>`
- Decorators: `@Authorize('admin')`, `@Mutation(() => CustomMessageDTO)`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @Args | `input` | `InputUUID` | `'input'` |

### Mutation deleteComment

- Source: `src/activity/activity.mutation.ts:182`
- Handler: `ActivityMutation.deleteComment`
- Declared return: `Promise<CustomMessageDTO>`
- Decorators: `@Authorize('user')`, `@Mutation(() => CustomMessageDTO)`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @Args | `input` | `InputUUID` | `'input'` |
| @GetUserId | `userId` | `string` | `` |

### Mutation deleteFeedHistoryEntry

- Source: `src/user-feed-queue/resolvers/user-feed-queue.mutation.ts:52`
- Handler: `UserFeedQueueMutationResolver.deleteFeedHistoryEntry`
- Declared return: `Promise<boolean>`
- Decorators: `@Mutation(() => Boolean)`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @GetUserId | `userId` | `string` | `` |
| @Args | `entryId` | `string` | `'entryId'` |

### Mutation deleteFile

- Source: `src/listing/listing.mutation.ts:221`
- Handler: `ListingMutation.deleteFile`
- Declared return: `Promise<CustomMessageDTO>`
- Decorators: `@Authorize('user')`, `@Mutation(() => CustomMessageDTO)`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @Args | `input` | `InputUUID` | `'input'` |
| @GetUserId | `userId` | `string` | `` |

### Mutation deleteFolder

- Source: `src/folder/resolvers/folder.mutation.ts:45`
- Handler: `FolderMutation.deleteFolder`
- Declared return: `Promise<boolean>`
- Decorators: `@Mutation(() => Boolean)`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @GetUserId | `userId` | `string` | `` |
| @Args | `folderId` | `string` | `'folderId', new ParseUUIDPipe()` |

### Mutation dequeueEntry

- Source: `src/user-feed-queue/resolvers/user-feed-queue.mutation.ts:23`
- Handler: `UserFeedQueueMutationResolver.dequeueEntry`
- Declared return: `Promise<boolean>`
- Decorators: `@Mutation(() => Boolean)`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @GetUserId | `userId` | `string` | `` |
| @Args | `entryId` | `string` | `'entryId'` |

### Mutation downgradeSubscription

- Source: `src/billing/billing.mutation.ts:92`
- Handler: `BillingMutation.downgradeSubscription`
- Declared return: `Promise<boolean>`
- Decorators: `@Mutation(() => Boolean)`, `@Authorize('user')`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @GetUserId | `userId` | `string` | `` |
| @Args | `plan` | `string` | `'plan', { type: () => String, nullable: false }` |

### Mutation enqueueTarget

- Source: `src/user-feed-queue/resolvers/user-feed-queue.mutation.ts:13`
- Handler: `UserFeedQueueMutationResolver.enqueueTarget`
- Declared return: `Promise<UserFeedQueueEntry>`
- Decorators: `@Mutation(() => UserFeedQueueEntry)`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @GetUserId | `userId` | `string` | `` |
| @Args | `targetType` | `FeedTargetType` | `'targetType', { type: () => FeedTargetType }` |
| @Args | `targetId` | `string` | `'targetId'` |

### Mutation followFolder

- Source: `src/folder/resolvers/folder.mutation.ts:178`
- Handler: `FolderMutation.followFolder`
- Declared return: `Promise<boolean>`
- Decorators: `@Mutation(() => Boolean)`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @GetUserId | `userId` | `string` | `` |
| @Args | `folderId` | `string` | `'folderId', new ParseUUIDPipe()` |

### Mutation generateRegistrationTokens

- Source: `src/user/user.mutation.ts:411`
- Handler: `UserMutation.generateRegistrationTokens`
- Declared return: `Promise<CustomMessageDTO>`
- Decorators: `@Authorize('admin')`, `@Mutation(() => CustomMessageDTO)`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @Args | `input` | `AdminGenerateRegistrationTokensDTO` | `'input'` |

### Mutation hideCommentAndFlags

- Source: `src/activity/activity.mutation.ts:226`
- Handler: `ActivityMutation.hideCommentAndFlags`
- Declared return: `Promise<CustomMessageDTO>`
- Decorators: `@Authorize('admin')`, `@Mutation(() => CustomMessageDTO)`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @Args | `input` | `InputUUID` | `'input'` |

### Mutation hideListingAndFlags

- Source: `src/listing/listing.mutation.ts:367`
- Handler: `ListingMutation.hideListingAndFlags`
- Declared return: `Promise<CustomMessageDTO>`
- Decorators: `@Authorize('admin')`, `@Mutation(() => CustomMessageDTO)`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @Args | `input` | `InputUUID` | `'input'` |

### Mutation ignoreCommentFlag

- Source: `src/activity/activity.mutation.ts:216`
- Handler: `ActivityMutation.ignoreCommentFlag`
- Declared return: `Promise<CustomMessageDTO>`
- Decorators: `@Authorize('admin')`, `@Mutation(() => CustomMessageDTO)`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @Args | `input` | `InputUUID` | `'input'` |

### Mutation ignoreListingFlag

- Source: `src/listing/listing.mutation.ts:357`
- Handler: `ListingMutation.ignoreListingFlag`
- Declared return: `Promise<CustomMessageDTO>`
- Decorators: `@Authorize('admin')`, `@Mutation(() => CustomMessageDTO)`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @Args | `input` | `InputUUID` | `'input'` |

### Mutation initListing

- Source: `src/listing/listing.mutation.ts:54`
- Handler: `ListingMutation.initListing`
- Declared return: `Promise<string>`
- Decorators: `@Throttle({ default: { limit: 10, ttl: 60000 } })`, `@Authorize('user')`, `@Mutation(() => String)`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @GetUserId | `userId` | `string` | `` |

### Mutation likeFolder

- Source: `src/folder/resolvers/folder.mutation.ts:142`
- Handler: `FolderMutation.likeFolder`
- Declared return: `Promise<boolean>`
- Decorators: `@Mutation(() => Boolean)`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @GetUserId | `userId` | `string` | `` |
| @Args | `folderId` | `string` | `'folderId', new ParseUUIDPipe()` |

### Mutation markMentionRead

- Source: `src/mention/mention.query.ts:38`
- Handler: `MentionQuery.markMentionRead`
- Declared return: `Promise<boolean>`
- Decorators: `@Authorize('user')`, `@Mutation(() => Boolean)`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @GetUserId | `userId` | `string` | `` |
| @Args | `mentionId` | `string` | `'mentionId'` |

### Mutation mintListing

- Source: `src/listing/listing.mutation.ts:72`
- Handler: `ListingMutation.mintListing`
- Declared return: `Promise<CustomMessageDTO>`
- Decorators: `@Authorize('user')`, `@Mutation(() => CustomMessageDTO)`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @Args | `assetId` | `string` | `'input'` |
| @GetUserId | `userId` | `string` | `` |

### Mutation moveListingToPortfolio

- Source: `src/folder/resolvers/folder.mutation.ts:54`
- Handler: `FolderMutation.moveListingToPortfolio`
- Declared return: `Promise<boolean>`
- Decorators: `@Mutation(() => Boolean)`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @GetUserId | `userId` | `string` | `` |
| @Args | `listingId` | `string` | `'listingId'` |
| @Args | `portfolioId` | `string` | `'portfolioId'` |

### Mutation notificationViewed

- Source: `src/notifications/notifications.mutation.ts:13`
- Handler: `NotificationsMutation.notificationViewed`
- Declared return: `Promise<CustomMessageDTO>`
- Decorators: `@Authorize('user')`, `@Mutation(() => CustomMessageDTO)`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @Args | `input` | `InputUUID` | `'input'` |
| @GetUserId | `userId` | `string` | `` |

### Mutation placeBid

- Source: `src/auction/auction.mutation.ts:27`
- Handler: `AuctionMutation.placeBid`
- Declared return: `Promise<CustomMessageDTO>`
- Decorators: `@Authorize('user')`, `@Mutation(() => CustomMessageDTO)`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @Args | `input` | `BidPlacedDTO` | `'input'` |

### Mutation publishListing

- Source: `src/listing/listing.mutation.ts:83`
- Handler: `ListingMutation.publishListing`
- Declared return: `Promise<PublishListingResultDTO>`
- Decorators: `@Authorize('user')`, `@UseGuards(MarketplaceEnabledGuard)`, `@Mutation(() => PublishListingResultDTO)`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @Args | `input` | `PublishListingDTO` | `'input'` |
| @GetUserId | `userId` | `string` | `` |

### Mutation purchaseListing

- Source: `src/listing/listing.mutation.ts:438`
- Handler: `ListingMutation.purchaseListing`
- Declared return: `Promise<PurchaseResultDTO>`
- Decorators: `@Authorize('user')`, `@UseGuards(MarketplaceEnabledGuard, PayPalConnectedGuard)`, `@Mutation(() => PurchaseResultDTO)`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @Args | `input` | `PurchaseListingInput` | `'input'` |
| @GetUserId | `userId` | `string` | `` |

### Mutation recoverComment

- Source: `src/activity/activity.mutation.ts:236`
- Handler: `ActivityMutation.recoverComment`
- Declared return: `Promise<CustomMessageDTO>`
- Decorators: `@Authorize('admin')`, `@Mutation(() => CustomMessageDTO)`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @Args | `input` | `InputUUID` | `'input'` |

### Mutation recoverListing

- Source: `src/listing/listing.mutation.ts:377`
- Handler: `ListingMutation.recoverListing`
- Declared return: `Promise<CustomMessageDTO>`
- Decorators: `@Authorize('admin')`, `@Mutation(() => CustomMessageDTO)`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @Args | `input` | `InputUUID` | `'input'` |

### Mutation redeemShare

- Source: `src/activity/activity.mutation.ts:103`
- Handler: `ActivityMutation.redeemShare`
- Declared return: `Promise<Share>`
- Decorators: `@Authorize('user')`, `@Mutation(() => Share)`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @Args | `input` | `RedeemShareDTO` | `'input'` |
| @GetUserId | `userId` | `string` | `` |

### Mutation regenerateRegisterPayPalSeller

- Source: `src/paypal/paypal.mutation.ts:29`
- Handler: `PayPalMutation.regenerateRegisterPayPalSeller`
- Declared return: `Promise<string>`
- Decorators: `@UseGuards(MarketplaceEnabledGuard)`, `@Authorize('user')`, `@Mutation(() => String)`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @GetUserId | `userId` | `string` | `` |

### Mutation registerListing

- Source: `src/listing/listing.mutation.ts:61`
- Handler: `ListingMutation.registerListing`
- Declared return: `Promise<string>`
- Decorators: `@Authorize('user')`, `@Mutation(() => String)`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @Args | `input` | `RegisterListingDTO` | `'input'` |
| @GetUserId | `userId` | `string` | `` |

### Mutation registerPayPalSeller

- Source: `src/paypal/paypal.mutation.ts:20`
- Handler: `PayPalMutation.registerPayPalSeller`
- Declared return: `Promise<string>`
- Decorators: `@UseGuards(MarketplaceEnabledGuard)`, `@Authorize('user')`, `@Mutation(() => String)`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @GetUserId | `userId` | `string` | `` |

### Mutation rejectListing

- Source: `src/listing/listing.mutation.ts:164`
- Handler: `ListingMutation.rejectListing`
- Declared return: `Promise<ListingDTO>`
- Decorators: `@Authorize('admin')`, `@Mutation(() => ListingDTO)`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @Args | `input` | `RejectListingDTO` | `'input'` |

### Mutation rejectUserWhitelistRequest

- Source: `src/activity/activity.mutation.ts:150`
- Handler: `ActivityMutation.rejectUserWhitelistRequest`
- Declared return: `Promise<CustomMessageDTO>`
- Decorators: `@Authorize('admin')`, `@Mutation(() => CustomMessageDTO)`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @Args | `input` | `RejectUserWhitelistRequestDTO` | `'input'` |

### Mutation rejectUserWhitelistRequestByAdmin

- Source: `src/activity/activity.mutation.ts:160`
- Handler: `ActivityMutation.rejectUserWhitelistRequestByAdmin`
- Declared return: `Promise<CustomMessageDTO>`
- Decorators: `@Authorize('admin')`, `@Mutation(() => CustomMessageDTO)`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @Args | `input` | `RejectUserWhitelistRequestByAdminDTO` | `'input'` |

### Mutation removeBid

- Source: `src/auction/auction.mutation.ts:14`
- Handler: `AuctionMutation.removeBid`
- Declared return: `Promise<CustomMessageDTO>`
- Decorators: `@Authorize('user')`, `@Mutation(() => CustomMessageDTO)`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @Args | `input` | `RemoveBidDTO` | `'input'` |
| @GetUserId | `userId` | `string` | `` |

### Mutation removeCategory

- Source: `src/listing/listing.mutation.ts:335`
- Handler: `ListingMutation.removeCategory`
- Declared return: `Promise<CustomMessageDTO>`
- Decorators: `@Authorize('admin')`, `@Mutation(() => CustomMessageDTO)`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @Args | `input` | `RemoveCategoryDTO` | `'input'` |

### Mutation removeListing

- Source: `src/listing/listing.mutation.ts:184`
- Handler: `ListingMutation.removeListing`
- Declared return: `Promise<CustomMessageDTO>`
- Decorators: `@Authorize('user')`, `@Mutation(() => CustomMessageDTO)`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @Args | `input` | `InputUUID` | `'input'` |
| @GetUserId | `userId` | `string` | `` |

### Mutation removeListingFromCollection

- Source: `src/folder/resolvers/folder.mutation.ts:83`
- Handler: `FolderMutation.removeListingFromCollection`
- Declared return: `Promise<boolean>`
- Decorators: `@Mutation(() => Boolean)`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @GetUserId | `userId` | `string` | `` |
| @Args | `listingId` | `string` | `'listingId'` |
| @Args | `collectionId` | `string` | `'collectionId'` |

### Mutation removeListingFromPortfolio

- Source: `src/folder/resolvers/folder.mutation.ts:64`
- Handler: `FolderMutation.removeListingFromPortfolio`
- Declared return: `Promise<boolean>`
- Decorators: `@Mutation(() => Boolean)`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @GetUserId | `userId` | `string` | `` |
| @Args | `listingId` | `string` | `'listingId'` |

### Mutation removeNotification

- Source: `src/notifications/notifications.mutation.ts:36`
- Handler: `NotificationsMutation.removeNotification`
- Declared return: `Promise<CustomMessageDTO>`
- Decorators: `@Authorize('admin')`, `@Mutation(() => CustomMessageDTO)`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @Args | `input` | `InputUUID` | `'input'` |

### Mutation removeOffer

- Source: `src/marketplace/marketplace.mutation.ts:24`
- Handler: `MarketplaceMutation.removeOffer`
- Declared return: `Promise<CustomMessageDTO>`
- Decorators: `@Authorize('user')`, `@Mutation(() => CustomMessageDTO)`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @Args | `input` | `RemoveOfferDTO` | `'input'` |
| @GetUserId | `userId` | `string` | `` |

### Mutation removePayToken

- Source: `src/listing/listing.mutation.ts:304`
- Handler: `ListingMutation.removePayToken`
- Declared return: `Promise<CustomMessageDTO>`
- Decorators: `@Authorize('user')`, `@Mutation(() => CustomMessageDTO)`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @Args | `input` | `InputETH` | `'input'` |
| @GetUserId | `userId` | `string` | `` |

### Mutation removeQA

- Source: `src/user/user.mutation.ts:355`
- Handler: `UserMutation.removeQA`
- Declared return: `Promise<CustomMessageDTO>`
- Decorators: `@Authorize('admin')`, `@Mutation(() => CustomMessageDTO)`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @Args | `input` | `InputNumber` | `'input'` |

### Mutation removeQuestionType

- Source: `src/user/user.mutation.ts:373`
- Handler: `UserMutation.removeQuestionType`
- Declared return: `Promise<CustomMessageDTO>`
- Decorators: `@Authorize('admin')`, `@Mutation(() => CustomMessageDTO)`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @Args | `input` | `InputNumber` | `'input'` |

### Mutation removeUnusedFiles

- Source: `src/listing/listing.mutation.ts:257`
- Handler: `ListingMutation.removeUnusedFiles`
- Declared return: `Promise<CustomMessageDTO>`
- Decorators: `@Authorize('user')`, `@Mutation(() => CustomMessageDTO)`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @GetUserId | `userId` | `string` | `` |

### Mutation reorderFolder

- Source: `src/folder/resolvers/folder.mutation.ts:113`
- Handler: `FolderMutation.reorderFolder`
- Declared return: `Promise<boolean>`
- Decorators: `@Mutation(() => Boolean)`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @GetUserId | `userId` | `string` | `` |
| @Args | `input` | `ReorderFolderPositionInput` | `'input'` |

### Mutation reorderFolderListing

- Source: `src/folder/resolvers/folder.mutation.ts:97`
- Handler: `FolderMutation.reorderFolderListing`
- Declared return: `Promise<boolean>`
- Decorators: `@Mutation(() => Boolean)`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @GetUserId | `userId` | `string` | `` |
| @Args | `folderId` | `string` | `'folderId', new ParseUUIDPipe()` |
| @Args | `input` | `ReorderFolderInput` | `'input'` |

### Mutation reorderQueueEntry

- Source: `src/user-feed-queue/resolvers/user-feed-queue.mutation.ts:31`
- Handler: `UserFeedQueueMutationResolver.reorderQueueEntry`
- Declared return: `Promise<boolean>`
- Decorators: `@Mutation(() => Boolean)`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @GetUserId | `userId` | `string` | `` |
| @Args | `input` | `ReorderQueueEntryInput` | `'input'` |

### Mutation requestBulkExport

- Source: `src/analytics/analytics.resolver.ts:186`
- Handler: `AnalyticsResolver.requestBulkExport`
- Declared return: `Promise<BulkExportStatusDTO>`
- Decorators: `@Authorize('user')`, `@CreditCost(50)`, `@Mutation(() => BulkExportStatusDTO)`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @GetUserId | `userId` | `string` | `` |
| @Args | `input` | `BulkExportRequestInput` | `'input'` |

### Mutation requestReprocessing

- Source: `src/listing/listing.mutation.ts:195`
- Handler: `ListingMutation.requestReprocessing`
- Declared return: `Promise<CustomMessageDTO>`
- Decorators: `@Authorize('user')`, `@Mutation(() => CustomMessageDTO)`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @Args | `input` | `InputUUID` | `'input'` |
| @GetUserId | `userId` | `string` | `` |

### Mutation resetNegativePoint

- Source: `src/user/user.mutation.ts:383`
- Handler: `UserMutation.resetNegativePoint`
- Declared return: `Promise<CustomMessageDTO>`
- Decorators: `@Authorize('admin')`, `@Mutation(() => CustomMessageDTO)`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @Args | `input` | `InputUUID` | `'input'` |

### Mutation resetUser2fa

- Source: `src/user/user.mutation.ts:312`
- Handler: `UserMutation.resetUser2fa`
- Declared return: `Promise<CustomMessageDTO>`
- Decorators: `@Authorize('admin')`, `@Mutation(() => CustomMessageDTO)`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @Args | `input` | `InputUUID` | `'input'` |

### Mutation retryDeadLetter

- Source: `src/resilience/outbox/outbox.resolver.ts:29`
- Handler: `OutboxResolver.retryDeadLetter`
- Declared return: `Promise<boolean>`
- Decorators: `@Authorize('admin')`, `@Mutation(() => Boolean)`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @Args | `outboxId` | `string` | `'outboxId'` |

### Mutation saveFolder

- Source: `src/folder/resolvers/folder.mutation.ts:160`
- Handler: `FolderMutation.saveFolder`
- Declared return: `Promise<boolean>`
- Decorators: `@Mutation(() => Boolean)`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @GetUserId | `userId` | `string` | `` |
| @Args | `folderId` | `string` | `'folderId', new ParseUUIDPipe()` |

### Mutation saveListingToCollection

- Source: `src/folder/resolvers/folder.mutation.ts:73`
- Handler: `FolderMutation.saveListingToCollection`
- Declared return: `Promise<boolean>`
- Decorators: `@Mutation(() => Boolean)`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @GetUserId | `userId` | `string` | `` |
| @Args | `listingId` | `string` | `'listingId'` |
| @Args | `collectionId` | `string` | `'collectionId'` |

### Mutation saveListingTxHash

- Source: `src/listing/listing.mutation.ts:267`
- Handler: `ListingMutation.saveListingTxHash`
- Declared return: `Promise<CustomMessageDTO>`
- Decorators: `@Authorize('user')`, `@Mutation(() => CustomMessageDTO)`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @Args | `input` | `TransactionHashDTO` | `'input'` |
| @GetUserId | `userId` | `string` | `` |

### Mutation savePayToken

- Source: `src/listing/listing.mutation.ts:315`
- Handler: `ListingMutation.savePayToken`
- Declared return: `Promise<CustomMessageDTO>`
- Decorators: `@Authorize('admin')`, `@Mutation(() => CustomMessageDTO)`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @Args | `input` | `CreatePayTokenDTO` | `'input'` |

### Mutation savePayTokenTxHash

- Source: `src/listing/listing.mutation.ts:289`
- Handler: `ListingMutation.savePayTokenTxHash`
- Declared return: `Promise<CustomMessageDTO>`
- Decorators: `@Authorize('user')`, `@Mutation(() => CustomMessageDTO)`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @Args | `input` | `UpdatePayTokenDTO` | `'input'` |
| @GetUserId | `userId` | `string` | `` |

### Mutation sendMemeToken

- Source: `src/listing/listing.mutation.ts:417`
- Handler: `ListingMutation.sendMemeToken`
- Declared return: `Promise<CustomMessageDTO>`
- Decorators: `@Authorize('admin')`, `@Mutation(() => CustomMessageDTO)`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @Args | `input` | `SendMemeTokenDTO` | `'input'` |

### Mutation setActiveQueueEntry

- Source: `src/user-feed-queue/resolvers/user-feed-queue.mutation.ts:39`
- Handler: `UserFeedQueueMutationResolver.setActiveQueueEntry`
- Declared return: `Promise<boolean>`
- Decorators: `@Mutation(() => Boolean)`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @GetUserId | `userId` | `string` | `` |
| @Args | `entryId` | `string` | `'entryId', { nullable: true }` |

### Mutation setAddERC20PlatformFee

- Source: `src/listing/listing.mutation.ts:407`
- Handler: `ListingMutation.setAddERC20PlatformFee`
- Declared return: `Promise<CustomMessageDTO>`
- Decorators: `@Authorize('admin')`, `@Mutation(() => CustomMessageDTO)`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @Args | `platformFee` | `string` | `'input'` |

### Mutation setAssetFlagReviewed

- Source: `src/listing/listing.mutation.ts:387`
- Handler: `ListingMutation.setAssetFlagReviewed`
- Declared return: `Promise<CustomMessageDTO>`
- Decorators: `@Authorize('admin')`, `@Mutation(() => CustomMessageDTO)`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @Args | `input` | `SetAssetFlagReviewedDTO` | `'input'` |

### Mutation setAssetUploaded

- Source: `src/listing/listing.mutation.ts:246`
- Handler: `ListingMutation.setAssetUploaded`
- Declared return: `Promise<CustomMessageDTO>`
- Decorators: `@Authorize('user')`, `@Mutation(() => CustomMessageDTO)`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @Args | `input` | `InputUUID` | `'input'` |
| @GetUserId | `userId` | `string` | `` |

### Mutation setDownloadPrice

- Source: `src/listing/listing.mutation.ts:427`
- Handler: `ListingMutation.setDownloadPrice`
- Declared return: `Promise<CustomMessageDTO>`
- Decorators: `@Authorize('user')`, `@UseGuards(MarketplaceEnabledGuard)`, `@Mutation(() => CustomMessageDTO)`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @Args | `input` | `SetDownloadPriceDTO` | `'input'` |
| @GetUserId | `userId` | `string` | `` |

### Mutation setFreeDownload

- Source: `src/listing/listing.mutation.ts:120`
- Handler: `ListingMutation.setFreeDownload`
- Declared return: `Promise<boolean>`
- Decorators: `@Authorize('user')`, `@Mutation(() => Boolean)`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @GetUserId | `userId` | `string` | `` |
| @Args | `listingId` | `string` | `'listingId'` |
| @Args | `freeDownload` | `boolean` | `'freeDownload'` |

### Mutation setListingVisibility

- Source: `src/listing/listing.mutation.ts:105`
- Handler: `ListingMutation.setListingVisibility`
- Declared return: `Promise<boolean>`
- Decorators: `@Authorize('user')`, `@Mutation(() => Boolean)`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @GetUserId | `userId` | `string` | `` |
| @Args | `listingId` | `string` | `'listingId'` |
| @Args | `isPrivate` | `boolean` | `'isPrivate'` |

### Mutation setSourceFileAsThumbnail

- Source: `src/listing/listing.mutation.ts:232`
- Handler: `ListingMutation.setSourceFileAsThumbnail`
- Declared return: `Promise<AssetDTO>`
- Decorators: `@Authorize('user')`, `@Mutation(() => AssetDTO)`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @Args | `input` | `InputUUID` | `'input'` |
| @GetUserId | `userId` | `string` | `` |

### Mutation setupCreditTopUp

- Source: `src/billing/billing.mutation.ts:142`
- Handler: `BillingMutation.setupCreditTopUp`
- Declared return: `Promise<CheckoutUrlDTO>`
- Decorators: `@Mutation(() => CheckoutUrlDTO)`, `@Authorize('user')`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @GetUserId | `userId` | `string` | `` |
| @GetUserEmail | `email` | `string` | `` |
| @Args | `tier` | `string` | `'tier', { type: () => String, nullable: false }` |

### Mutation switchBillingInterval

- Source: `src/billing/billing.mutation.ts:113`
- Handler: `BillingMutation.switchBillingInterval`
- Declared return: `Promise<CheckoutUrlDTO>`
- Decorators: `@Mutation(() => CheckoutUrlDTO)`, `@Authorize('user')`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @GetUserId | `userId` | `string` | `` |
| @Args | `interval` | `string` | `'interval', { type: () => String }` |

### Mutation toggleFavorite

- Source: `src/folder/resolvers/folder.mutation.ts:127`
- Handler: `FolderMutation.toggleFavorite`
- Declared return: `Promise<boolean>`
- Decorators: `@Mutation(() => Boolean)`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @GetUserId | `userId` | `string` | `` |
| @Args | `listingId` | `string` | `'listingId'` |

### Mutation toggleUserFavorite

- Source: `src/activity/activity.mutation.ts:59`
- Handler: `ActivityMutation.toggleUserFavorite`
- Declared return: `Promise<CustomMessageDTO>`
- Decorators: `@Authorize('user')`, `@Mutation(() => CustomMessageDTO)`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @Args | `input` | `InputUUID` | `'input'` |
| @GetUserId | `userId` | `string` | `` |

### Mutation toggleUserFollow

- Source: `src/activity/activity.mutation.ts:48`
- Handler: `ActivityMutation.toggleUserFollow`
- Declared return: `Promise<UserFollowDTO>`
- Decorators: `@Authorize('user')`, `@Mutation(() => CustomMessageDTO)`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @Args | `input` | `InputUUID` | `'input'` |
| @GetUserId | `userId` | `string` | `` |

### Mutation toggleUserLike

- Source: `src/activity/activity.mutation.ts:37`
- Handler: `ActivityMutation.toggleUserLike`
- Declared return: `Promise<CustomMessageDTO>`
- Decorators: `@Authorize('user')`, `@Mutation(() => CustomMessageDTO)`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @Args | `input` | `InputUUID` | `'input'` |
| @GetUserId | `userId` | `string` | `` |

### Mutation unfollowFolder

- Source: `src/folder/resolvers/folder.mutation.ts:187`
- Handler: `FolderMutation.unfollowFolder`
- Declared return: `Promise<boolean>`
- Decorators: `@Mutation(() => Boolean)`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @GetUserId | `userId` | `string` | `` |
| @Args | `folderId` | `string` | `'folderId', new ParseUUIDPipe()` |

### Mutation unlikeFolder

- Source: `src/folder/resolvers/folder.mutation.ts:151`
- Handler: `FolderMutation.unlikeFolder`
- Declared return: `Promise<boolean>`
- Decorators: `@Mutation(() => Boolean)`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @GetUserId | `userId` | `string` | `` |
| @Args | `folderId` | `string` | `'folderId', new ParseUUIDPipe()` |

### Mutation unlinkAgent

- Source: `src/user/user.mutation.ts:119`
- Handler: `UserMutation.unlinkAgent`
- Declared return: `Promise<boolean>`
- Decorators: `@Authorize('user')`, `@Mutation(() => Boolean)`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @Context | `context` | `any` | `` |

### Mutation unpublishListing

- Source: `src/listing/listing.mutation.ts:93`
- Handler: `ListingMutation.unpublishListing`
- Declared return: `Promise<CustomMessageDTO>`
- Decorators: `@Authorize('user')`, `@UseGuards(MarketplaceEnabledGuard)`, `@Mutation(() => CustomMessageDTO)`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @Args | `listingId` | `string` | `'input'` |
| @GetUserId | `userId` | `string` | `` |

### Mutation unsaveFolder

- Source: `src/folder/resolvers/folder.mutation.ts:169`
- Handler: `FolderMutation.unsaveFolder`
- Declared return: `Promise<boolean>`
- Decorators: `@Mutation(() => Boolean)`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @GetUserId | `userId` | `string` | `` |
| @Args | `folderId` | `string` | `'folderId', new ParseUUIDPipe()` |

### Mutation updateAiModel

- Source: `src/ai-model/ai-model.mutation.ts:23`
- Handler: `AiModelMutation.updateAiModel`
- Declared return: `Promise<AiModelResponseDTO>`
- Decorators: `@Authorize('admin')`, `@Mutation(() => AiModelResponseDTO)`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @Args | `input` | `UpdateAiModelDTO` | `'input'` |

### Mutation updateConfigAmount

- Source: `src/config/config.mutation.ts:15`
- Handler: `ConfigMutation.updateConfigAmount`
- Declared return: `Promise<Config>`
- Decorators: `@Authorize('admin')`, `@Mutation(() => Config)`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @Args | `input` | `ConfigValueDTO` | `'input'` |

### Mutation updateCreatorStatus

- Source: `src/user/user.mutation.ts:260`
- Handler: `UserMutation.updateCreatorStatus`
- Declared return: `Promise<CreatorStatus>`
- Decorators: `@Authorize('admin')`, `@Mutation(() => CreatorStatus)`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @Args | `input` | `AdminUpdateUserStatusDTO` | `'input'` |

### Mutation updateFolder

- Source: `src/folder/resolvers/folder.mutation.ts:36`
- Handler: `FolderMutation.updateFolder`
- Declared return: `Promise<Folder>`
- Decorators: `@Mutation(() => Folder)`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @GetUserId | `userId` | `string` | `` |
| @Args | `folderId` | `string` | `'folderId', new ParseUUIDPipe()` |
| @Args | `input` | `UpdateFolderInput` | `'input'` |

### Mutation updateListing

- Source: `src/listing/listing.mutation.ts:143`
- Handler: `ListingMutation.updateListing`
- Declared return: `Promise<string>`
- Decorators: `@Authorize('admin')`, `@Mutation(() => String)`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @Args | `input` | `RegisterListingDTO` | `'input'` |

### Mutation updateListingPrice

- Source: `src/listing/listing.mutation.ts:131`
- Handler: `ListingMutation.updateListingPrice`
- Declared return: `Promise<CustomMessageDTO>`
- Decorators: `@Authorize('user')`, `@UseGuards(MarketplaceEnabledGuard)`, `@Mutation(() => CustomMessageDTO)`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @Args | `input` | `PublishListingDTO` | `'input'` |
| @GetUserId | `userId` | `string` | `` |

### Mutation updateNotificationSettingChannel

- Source: `src/notifications/notifications.mutation.ts:26`
- Handler: `NotificationsMutation.updateNotificationSettingChannel`
- Declared return: `Promise<CustomMessageDTO>`
- Decorators: `@Authorize('user')`, `@Mutation(() => CustomMessageDTO)`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @Args | `input` | `UpdateNotificationSettingChannelDTO` | `'input'` |
| @GetUserId | `userId` | `string` | `` |

### Mutation updatePointAmount

- Source: `src/point/point.mutation.ts:28`
- Handler: `PointMutation.updatePointAmount`
- Declared return: `Promise<PointType>`
- Decorators: `@Authorize('admin')`, `@Mutation(() => PointType)`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @Args | `input` | `PointTypeDTO` | `'input'` |

### Mutation updateSocialMedia

- Source: `src/user/user.mutation.ts:228`
- Handler: `UserMutation.updateSocialMedia`
- Declared return: `Promise<CreatorStatusDTO>`
- Decorators: `@Authorize('user')`, `@Mutation(() => CreatorStatusDTO)`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @Args | `input` | `SocialMediaDTO` | `'input'` |
| @GetUserId | `userId` | `string` | `` |

### Mutation updateUserRole

- Source: `src/user/user.mutation.ts:270`
- Handler: `UserMutation.updateUserRole`
- Declared return: `Promise<CustomMessageDTO>`
- Decorators: `@Authorize('admin')`, `@Mutation(() => CustomMessageDTO)`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @Args | `input` | `AdminUpdateUserRoleDTO` | `'input'` |

### Mutation updateUserStatus

- Source: `src/user/user.mutation.ts:250`
- Handler: `UserMutation.updateUserStatus`
- Declared return: `Promise<UserStatus>`
- Decorators: `@Authorize('admin')`, `@Mutation(() => UserStatus)`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @Args | `input` | `AdminUpdateUserStatusDTO` | `'input'` |

### Mutation upgradeSubscription

- Source: `src/billing/billing.mutation.ts:60`
- Handler: `BillingMutation.upgradeSubscription`
- Declared return: `Promise<CheckoutUrlDTO>`
- Decorators: `@Mutation(() => CheckoutUrlDTO)`, `@Authorize('user')`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @GetUserId | `userId` | `string` | `` |
| @Args | `plan` | `string` | `'plan', { type: () => String, nullable: false }` |
| @Args | `interval` | `string` | `'interval', { type: () => String, nullable: true }` |

### Mutation userAcceptPassword

- Source: `src/user/user.mutation.ts:183`
- Handler: `UserMutation.userAcceptPassword`
- Declared return: `Promise<CustomMessageDTO>`
- Decorators: `@Mutation(() => CustomMessageDTO)`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @Args | `input` | `UserChangePassDTO` | `'input'` |

### Mutation userChangePassword

- Source: `src/user/user.mutation.ts:194`
- Handler: `UserMutation.userChangePassword`
- Declared return: `Promise<CustomMessageDTO>`
- Decorators: `@Authorize('user')`, `@Mutation(() => CustomMessageDTO)`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @Args | `input` | `UserChangePasswordDTO` | `'input'` |
| @Context | `context` | `any` | `` |

### Mutation userCheck2faCode

- Source: `src/user/user.mutation.ts:296`
- Handler: `UserMutation.userCheck2faCode`
- Declared return: `Promise<string>`
- Decorators: `@Authorize('user')`, `@Mutation(() => String)`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @Args | `input` | `Check2faDTO` | `'input'` |
| @GetUserId | `userId` | `string` | `` |
| @Context | `context` | `any` | `` |

### Mutation userConfirmEmail

- Source: `src/user/user.mutation.ts:150`
- Handler: `UserMutation.userConfirmEmail`
- Declared return: `Promise<CustomMessageDTO>`
- Decorators: `@Mutation(() => CustomMessageDTO)`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @Args | `input` | `string` | `'input'` |

### Mutation userFetchQrCode

- Source: `src/user/user.mutation.ts:280`
- Handler: `UserMutation.userFetchQrCode`
- Declared return: `Promise<User2faCodeDTO>`
- Decorators: `@Authorize('user')`, `@Mutation(() => User2faCodeDTO)`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @Args | `password` | `string` | `'password'` |
| @GetUserId | `userId` | `string` | `` |
| @Context | `context` | `any` | `` |

### Mutation userLogin

- Source: `src/user/user.mutation.ts:70`
- Handler: `UserMutation.userLogin`
- Declared return: `Promise<UserLoginResponse>`
- Decorators: `@Mutation(() => UserLoginResponse)`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @Args | `input` | `UserLoginDTO` | `'input'` |
| @Context | `context` | `any` | `` |

### Mutation userLogout

- Source: `src/user/user.mutation.ts:99`
- Handler: `UserMutation.userLogout`
- Declared return: `Promise<boolean>`
- Decorators: `@Authorize('user')`, `@Mutation(() => Boolean)`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @Context | `context` | `any` | `` |

### Mutation userResendVerificationEmail

- Source: `src/user/user.mutation.ts:161`
- Handler: `UserMutation.userResendVerificationEmail`
- Declared return: `Promise<CustomMessageDTO>`
- Decorators: `@Mutation(() => CustomMessageDTO)`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @Args | `input` | `UserEmailDTO` | `'input'` |

### Mutation userResetPassword

- Source: `src/user/user.mutation.ts:172`
- Handler: `UserMutation.userResetPassword`
- Declared return: `Promise<CustomMessageDTO>`
- Decorators: `@Mutation(() => CustomMessageDTO)`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @Args | `input` | `UserEmailDTO` | `'input'` |

### Mutation userSetUsername

- Source: `src/user/user.mutation.ts:219`
- Handler: `UserMutation.userSetUsername`
- Declared return: `Promise<PrivateUser>`
- Decorators: `@Authorize('user')`, `@Mutation(() => PrivateUser)`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @Args | `userName` | `string` | `'userName'` |
| @GetUserId | `userId` | `string` | `` |

### Mutation userSignup

- Source: `src/user/user.mutation.ts:57`
- Handler: `UserMutation.userSignup`
- Declared return: `Promise<UserLoginResponse>`
- Decorators: `@Mutation(() => UserLoginResponse)`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @Args | `input` | `UserSignupDTO` | `'input'` |

### Mutation userUpdateAccount

- Source: `src/user/user.mutation.ts:208`
- Handler: `UserMutation.userUpdateAccount`
- Declared return: `Promise<PrivateUser>`
- Decorators: `@Authorize('user')`, `@Mutation(() => PrivateUser)`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @Args | `input` | `UserUpdateAccountDTO` | `'input'` |
| @GetUserId | `userId` | `string` | `` |

### Mutation userUpdateNotificationSetting

- Source: `src/user/user.mutation.ts:239`
- Handler: `UserMutation.userUpdateNotificationSetting`
- Declared return: `Promise<CustomMessageDTO>`
- Decorators: `@Authorize('user')`, `@Mutation(() => CustomMessageDTO)`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @Args | `input` | `UserUpdateNotificationSettingDTO` | `'input'` |
| @GetUserId | `userId` | `string` | `` |

### Mutation userView

- Source: `src/activity/activity.mutation.ts:70`
- Handler: `ActivityMutation.userView`
- Declared return: `Promise<CustomMessageDTO>`
- Decorators: `@ApplyTokenInfo`, `@Mutation(() => CustomMessageDTO)`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @Args | `input` | `AddViewDTO` | `'input'` |
| @GetUserId | `userId` | `string` | `` |

### Mutation userWhitelistRequest

- Source: `src/activity/activity.mutation.ts:81`
- Handler: `ActivityMutation.userWhitelistRequest`
- Declared return: `Promise<CustomMessageDTO>`
- Decorators: `@Authorize('user')`, `@Mutation(() => CustomMessageDTO)`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @Args | `input` | `UserWhitelistRequestDTO` | `'input'` |
| @GetUserId | `userId` | `string` | `` |

### Mutation validatePayPalCapture

- Source: `src/paypal/paypal.mutation.ts:92`
- Handler: `PayPalMutation.validatePayPalCapture`
- Declared return: `Promise<boolean>`
- Decorators: `@UseGuards(MarketplaceEnabledGuard)`, `@Authorize('user')`, `@Mutation(() => Boolean)`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @Args | `input` | `ValidatePayPalCaptureDTO` | `'input'` |

### Mutation verifyMetamask

- Source: `src/user/user.mutation.ts:322`
- Handler: `UserMutation.verifyMetamask`
- Declared return: `Promise<VerifyMetamaskResponseDTO>`
- Decorators: `@Authorize('user')`, `@Mutation(() => VerifyMetamaskResponseDTO)`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @Args | `input` | `VerifyMetamaskDTO` | `'input'` |
| @GetUserId | `userId` | `string` | `` |

### Mutation verifyPayPalKYC

- Source: `src/paypal/paypal.mutation.ts:40`
- Handler: `PayPalMutation.verifyPayPalKYC`
- Declared return: `Promise<PayPalOnboardingStatusDTO>`
- Decorators: `@UseGuards(MarketplaceEnabledGuard)`, `@Authorize('user')`, `@Mutation(() => PayPalOnboardingStatusDTO)`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @GetUserId | `userId` | `string` | `` |

### Mutation whitelistUser

- Source: `src/activity/activity.mutation.ts:130`
- Handler: `ActivityMutation.whitelistUser`
- Declared return: `Promise<AdminUser>`
- Decorators: `@Authorize('admin')`, `@Mutation(() => AdminUser)`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @Args | `input` | `WhitelistUserDTO` | `'input'` |

### Mutation whitelistUserByRequestId

- Source: `src/activity/activity.mutation.ts:140`
- Handler: `ActivityMutation.whitelistUserByRequestId`
- Declared return: `Promise<CustomMessageDTO>`
- Decorators: `@Authorize('admin')`, `@Mutation(() => CustomMessageDTO)`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @Args | `input` | `InputUUID` | `'input'` |

### Query adminGetBillingSubscription

- Source: `src/billing/billing-admin.query.ts:10`
- Handler: `BillingAdminQuery.adminGetBillingSubscription`
- Declared return: `Promise<AdminBillingSubscriptionDTO>`
- Decorators: `@Authorize('admin')`, `@Query(() => AdminBillingSubscriptionDTO)`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @Args | `userId` | `string` | `'userId'` |

### Query checkAssetsReady

- Source: `src/listing/listing.query.ts:275`
- Handler: `ListingQuery.checkAssetsReady`
- Declared return: `Promise<AssetDTO[]>`
- Decorators: `@Authorize('user')`, `@Query(() => [AssetDTO])`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @Args | `input` | `InputArrayUUID` | `'input'` |
| @GetUserId | `userId` | `string` | `` |

### Query checkAssetStatus

- Source: `src/listing/listing.query.ts:139`
- Handler: `ListingQuery.checkAssetStatus`
- Declared return: `Promise<AssetStatusResponse>`
- Decorators: `@ApplyTokenInfo`, `@Query(() => AssetStatusResponse)`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @Args | `input` | `InputUUID` | `'input', { type: () => InputUUID }` |
| @GetUserId | `userId` | `string` | `` |

### Query checkIfWalletIsVerifiedByUser

- Source: `src/user/user.query.ts:258`
- Handler: `UserQuery.checkIfWalletIsVerifiedByUser`
- Declared return: `Promise<WalletVerifiedResponseDTO>`
- Decorators: `@Authorize('user')`, `@Query(() => WalletVerifiedResponseDTO)`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @Args | `walletAddress` | `WalletAddressDTO` | `'wallet_address'` |
| @GetUserId | `userId` | `string` | `` |

### Query checkUserLimit

- Source: `src/user/user.query.ts:306`
- Handler: `UserQuery.checkUserLimit`
- Declared return: `Promise<UserLimitResponseDTO>`
- Decorators: `@Query(() => UserLimitResponseDTO)`

Arguments/context bindings:

_None declared._

### Query checkUsernameAvailable

- Source: `src/user/user.query.ts:311`
- Handler: `UserQuery.checkUsernameAvailable`
- Declared return: `Promise<boolean>`
- Decorators: `@Query(() => Boolean)`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @Args | `userName` | `string` | `'userName'` |

### Query communityExists

- Source: `src/listing/listing.query.ts:376`
- Handler: `ListingQuery.communityExists`
- Declared return: `Promise<boolean>`
- Decorators: `@Authorize('user')`, `@Query(() => Boolean)`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @Args | `input` | `InputName` | `'input'` |

### Query fetchAllTiers

- Source: `src/permissions/permissions.query.ts:10`
- Handler: `PermissionsQuery.fetchAllTiers`
- Declared return: `Promise<TierConfigDTO>`
- Decorators: `@Query(() => TierConfigDTO)`

Arguments/context bindings:

_None declared._

### Query fetchCategories

- Source: `src/listing/listing.query.ts:325`
- Handler: `ListingQuery.fetchCategories`
- Declared return: `Promise<Category[]>`
- Decorators: `@Query(() => [Category])`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @Args | `parent` | `boolean` | `'parent', { nullable: true }` |

### Query fetchContractTypes

- Source: `src/listing/listing.query.ts:341`
- Handler: `ListingQuery.fetchContractTypes`
- Declared return: `Promise<ContractType[]>`
- Decorators: `@Query(() => [ContractType])`

Arguments/context bindings:

_None declared._

### Query fetchFlaggedListings

- Source: `src/search/search.resolver.ts:37`
- Handler: `SearchResolver.fetchFlaggedListings`
- Declared return: `Promise<ListingResponseWithTotalDTO>`
- Decorators: `@Authorize('admin')`, `@Query(() => ListingResponseWithTotalDTO)`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @Args | `input` | `FetchFlaggedListingsDTO` | `'input'` |

### Query fetchInitDraftListing

- Source: `src/listing/listing.query.ts:267`
- Handler: `ListingQuery.fetchInitDraftListing`
- Declared return: `Promise<ListingDTO | null>`
- Decorators: `@Authorize('user')`, `@Query(() => ListingDTO, { nullable: true })`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @GetUserId | `userId` | `string` | `` |

### Query fetchListingCount

- Source: `src/listing/listing.query.ts:311`
- Handler: `ListingQuery.fetchListingCount`
- Declared return: `Promise<Number>`
- Decorators: `@ApplyTokenInfo`, `@Query(() => Number)`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @Args | `input` | `WalletAddressDTO` | `'input'` |
| @GetUserId | `userId` | `string` | `` |

### Query fetchListings

- Source: `src/listing/listing.query.ts:200`
- Handler: `ListingQuery.fetchListings`
- Declared return: `Promise<ListingResponseWithTotalDTO>`
- Decorators: `@ApplyTokenInfo`, `@Query(() => ListingResponseWithTotalDTO)`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @Args | `input` | `FetchListingsDTO` | `'input'` |
| @GetUserId | `userId` | `string` | `` |

### Query fetchListingsByIds

- Source: `src/listing/listing.query.ts:228`
- Handler: `ListingQuery.fetchListingsByIds`
- Declared return: `Promise<ListingDTO[]>`
- Decorators: `@ApplyTokenInfo`, `@Query(() => [ListingDTO])`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @Args | `listingIds` | `string[]` | `'input', { type: () => [String] }` |
| @GetUserId | `userId` | `string` | `` |

### Query fetchListingsByUser

- Source: `src/listing/listing.query.ts:242`
- Handler: `ListingQuery.fetchListingsByUser`
- Declared return: `Promise<PaginatedListingsDTO>`
- Decorators: `@Authorize('user')`, `@Query(() => PaginatedListingsDTO)`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @GetUserId | `userId` | `string` | `` |
| @Args | `cursor` | `string` | `'cursor', { nullable: true }` |
| @Args | `limit` | `number` | `'limit', { nullable: true, defaultValue: 20 }` |
| @Args | `onlyDrafts` | `boolean` | `'onlyDrafts', { nullable: true, defaultValue: false }` |

### Query fetchListingsCursor

- Source: `src/search/search.resolver.ts:138`
- Handler: `SearchResolver.fetchListingsCursor`
- Declared return: `Promise<PaginatedListings>`
- Decorators: `@ApplyTokenInfo`, `@Query(() => PaginatedListings)`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @Args | `input` | `FetchListingsCursorDTO` | `'input'` |
| @GetUserId | `userId` | `string` | `` |

### Query fetchListingStatus

- Source: `src/listing/listing.query.ts:286`
- Handler: `ListingQuery.fetchListingStatus`
- Declared return: `Promise<ListingStatusResponseDTO>`
- Decorators: `@Authorize('user')`, `@Query(() => ListingStatusResponseDTO)`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @Args | `listingId` | `InputUUID` | `'input'` |
| @GetUserId | `userId` | `string` | `` |

### Query fetchListingStatuses

- Source: `src/listing/listing.query.ts:334`
- Handler: `ListingQuery.fetchListingStatuses`
- Declared return: `Promise<ListingStatus[]>`
- Decorators: `@Query(() => [ListingStatus])`

Arguments/context bindings:

_None declared._

### Query fetchPayToken

- Source: `src/listing/listing.query.ts:443`
- Handler: `ListingQuery.fetchPayToken`
- Declared return: `Promise<PayToken>`
- Decorators: `@Authorize('user')`, `@Query(() => PayToken)`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @GetUserId | `userId` | `string` | `` |

### Query fetchPayTokens

- Source: `src/listing/listing.query.ts:451`
- Handler: `ListingQuery.fetchPayTokens`
- Declared return: `Promise<PayToken[]>`
- Decorators: `@Query(() => [PayToken])`

Arguments/context bindings:

_None declared._

### Query findAllUserNotifications

- Source: `src/notifications/notifications.query.ts:15`
- Handler: `NotificationsQuery.findAllUserNotifications`
- Declared return: `Promise<NotificationReponseWithTotalDTO>`
- Decorators: `@Authorize('user')`, `@Query(() => NotificationReponseWithTotalDTO)`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @Args | `input` | `FindNotificationDTO` | `'input'` |
| @GetUserId | `userId` | `string` | `` |

### Query folder

- Source: `src/folder/resolvers/folder.query.ts:67`
- Handler: `FolderQuery.folder`
- Declared return: `Promise<Folder>`
- Decorators: `@ApplyTokenInfo`, `@Query(() => Folder, { nullable: true })`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @Args | `id` | `string` | `'id'` |
| @GetUserId | `userId` | `string` | `` |

### Query folderListings

- Source: `src/folder/resolvers/folder.query.ts:81`
- Handler: `FolderQuery.folderListings`
- Declared return: `Promise<PaginatedFolderListings>`
- Decorators: `@ApplyTokenInfo`, `@Query(() => PaginatedFolderListings)`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @GetUserId | `userId` | `string \| undefined` | `` |
| @Args | `folderId` | `string` | `'folderId'` |
| @Args | `cursor` | `string` | `'cursor', { nullable: true }` |
| @Args | `limit` | `number` | `'limit', { type: () => Int, nullable: true, defaultValue: 50 }` |
| @Args | `isPrivate` | `boolean` | `'isPrivate', { type: () => Boolean, nullable: true }` |

### Query getActiveAiModels

- Source: `src/ai-model/ai-model.query.ts:13`
- Handler: `AiModelQuery.getActiveAiModels`
- Declared return: `Promise<AiModelResponseDTO[]>`
- Decorators: `@Query(() => [AiModelResponseDTO])`

Arguments/context bindings:

_None declared._

### Query getActivePurchaseSession

- Source: `src/paypal/paypal.mutation.ts:127`
- Handler: `PayPalMutation.getActivePurchaseSession`
- Declared return: `Promise<BuyLinkDTO | null>`
- Decorators: `@UseGuards(MarketplaceEnabledGuard)`, `@Authorize('user')`, `@Query(() => BuyLinkDTO, { nullable: true })`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @Args | `input` | `InputUUID` | `'input'` |
| @GetUserId | `userId` | `string` | `` |

### Query getAddERC20PlatformFee

- Source: `src/listing/listing.query.ts:384`
- Handler: `ListingQuery.getAddERC20PlatformFee`
- Declared return: `Promise<number>`
- Decorators: `@Authorize('admin')`, `@Query(() => Number)`

Arguments/context bindings:

_None declared._

### Query getAdminComments

- Source: `src/activity/activity.query.ts:221`
- Handler: `ActivityQuery.getAdminComments`
- Declared return: `Promise<CommentReponseWithTotalDTO>`
- Decorators: `@Authorize('admin')`, `@Query(() => CommentReponseWithTotalDTO)`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @Args | `input` | `GetAdminCommentsDTO` | `'input'` |

### Query getAgentPerformance

- Source: `src/analytics/analytics.resolver.ts:168`
- Handler: `AnalyticsResolver.getAgentPerformance`
- Declared return: `Promise<AgentPerformanceDTO>`
- Decorators: `@CreditCost(30)`, `@Query(() => AgentPerformanceDTO)`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @Args | `period` | `string` | `'period', { defaultValue: '7d' }` |

### Query getAgentSuccessRate

- Source: `src/analytics/analytics.resolver.ts:176`
- Handler: `AnalyticsResolver.getAgentSuccessRate`
- Declared return: `Promise<AgentSuccessRateDTO>`
- Decorators: `@CreditCost(15)`, `@Query(() => AgentSuccessRateDTO)`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @Args | `userId` | `string` | `'userId'` |

### Query getAiModels

- Source: `src/ai-model/ai-model.query.ts:18`
- Handler: `AiModelQuery.getAiModels`
- Declared return: `Promise<AiModelResponseDTO[]>`
- Decorators: `@Authorize('admin')`, `@Query(() => [AiModelResponseDTO])`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @Args | `categoryId` | `number` | `'categoryId', { type: () => Int, nullable: true }` |

### Query getAllPointEarned

- Source: `src/point/point.query.ts:34`
- Handler: `PointQuery.getAllPointEarned`
- Declared return: `Promise<AllPointEarnedWithTotalDTO>`
- Decorators: `@Authorize('admin')`, `@Query(() => AllPointEarnedWithTotalDTO)`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @Args | `input` | `GetAllPointEarnedDTO` | `'input'` |

### Query getAllUsers

- Source: `src/user/user.query.ts:198`
- Handler: `UserQuery.getAllUsers`
- Declared return: `Promise<GetAllUsersReponseWithTotalDTO>`
- Decorators: `@Authorize('admin')`, `@Query(() => GetAllUsersReponseWithTotalDTO)`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @Args | `input` | `GetAllUsersDTO` | `'input'` |

### Query getAllUsersWithSocialMedia

- Source: `src/user/user.query.ts:208`
- Handler: `UserQuery.getAllUsersWithSocialMedia`
- Declared return: `Promise<GetAllUsersReponseWithTotalDTO>`
- Decorators: `@Authorize('admin')`, `@Query(() => GetAllUsersReponseWithTotalDTO)`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @Args | `input` | `GetAllUsersDTO` | `'input'` |

### Query getAllWaitlist

- Source: `src/user/user.query.ts:167`
- Handler: `UserQuery.getAllWaitlist`
- Declared return: `Promise<Waitlist[]>`
- Decorators: `@Authorize('admin')`, `@Query(() => [Waitlist])`

Arguments/context bindings:

_None declared._

### Query getArtistViralListings

- Source: `src/listing/listing.query.ts:157`
- Handler: `ListingQuery.getArtistViralListings`
- Declared return: `Promise<ListingDTO[]>`
- Decorators: `@Authorize('user')`, `@CheckPermission(PermissionAction.VIEW_VIRAL_SCORE)`, `@Query(() => [ListingDTO])`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @GetUserId | `userId` | `string` | `` |

### Query getAssetAccess

- Source: `src/listing/listing.query.ts:148`
- Handler: `ListingQuery.getAssetAccess`
- Declared return: `Promise<AssetAccessResponse>`
- Decorators: `@ApplyTokenInfo`, `@Query(() => AssetAccessResponse)`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @Args | `input` | `InputUUID` | `'input', { type: () => InputUUID }` |
| @GetUserId | `userId` | `string` | `` |

### Query getAssetFlags

- Source: `src/listing/listing.query.ts:392`
- Handler: `ListingQuery.getAssetFlags`
- Declared return: `Promise<AssetFlagResponseWithTotalDTO>`
- Decorators: `@Authorize('admin')`, `@Query(() => AssetFlagResponseWithTotalDTO)`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @Args | `input` | `GetAdminAssetsDTO` | `'input'` |

### Query getBidsTotal

- Source: `src/auction/auction.query.ts:48`
- Handler: `AuctionQuery.getBidsTotal`
- Declared return: `Promise<BidsTotalDTO>`
- Decorators: `@Authorize('user')`, `@Query(() => BidsTotalDTO)`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @GetUserId | `userId` | `string` | `` |

### Query getBidWars

- Source: `src/analytics/analytics.resolver.ts:109`
- Handler: `AnalyticsResolver.getBidWars`
- Declared return: `Promise<TrendingListingsDTO>`
- Decorators: `@CreditCost(10)`, `@Query(() => TrendingListingsDTO)`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @Args | `limit` | `number` | `'limit', { type: () => Int, defaultValue: 10 }` |

### Query getCategoryRanking

- Source: `src/analytics/analytics.resolver.ts:136`
- Handler: `AnalyticsResolver.getCategoryRanking`
- Declared return: `Promise<CategoryStatsDTO[]>`
- Decorators: `@CreditCost(20)`, `@Query(() => [CategoryStatsDTO])`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @Args | `period` | `string` | `'period', { defaultValue: '7d' }` |
| @Args | `sortBy` | `string` | `'sortBy', { defaultValue: 'revenue' }` |
| @Args | `limit` | `number` | `'limit', { type: () => Int, defaultValue: 10 }` |

### Query getCategoryStats

- Source: `src/analytics/analytics.resolver.ts:127`
- Handler: `AnalyticsResolver.getCategoryStats`
- Declared return: `Promise<CategoryStatsDTO>`
- Decorators: `@CreditCost(15)`, `@Query(() => CategoryStatsDTO)`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @Args | `categoryId` | `number` | `'categoryId', { type: () => Int }` |
| @Args | `period` | `string` | `'period', { defaultValue: '7d' }` |

### Query getCommentFlags

- Source: `src/activity/activity.query.ts:231`
- Handler: `ActivityQuery.getCommentFlags`
- Declared return: `Promise<CommentFlagDTO[]>`
- Decorators: `@Authorize('admin')`, `@Query(() => [CommentFlagDTO])`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @Args | `input` | `InputUUID` | `'input'` |

### Query getConfigs

- Source: `src/config/config.query.ts:24`
- Handler: `ConfigQuery.getConfigs`
- Declared return: `Promise<Config[]>`
- Decorators: `@Query(() => [Config])`

Arguments/context bindings:

_None declared._

### Query getCreatorAnalytics

- Source: `src/analytics/analytics.resolver.ts:59`
- Handler: `AnalyticsResolver.getCreatorAnalytics`
- Declared return: `Promise<CreatorAnalyticsDTO>`
- Decorators: `@CreditCost(15)`, `@Query(() => CreatorAnalyticsDTO)`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @Args | `userId` | `string` | `'userId'` |

### Query getCreatorLeaderboard

- Source: `src/analytics/analytics.resolver.ts:148`
- Handler: `AnalyticsResolver.getCreatorLeaderboard`
- Declared return: `Promise<LeaderboardDTO>`
- Decorators: `@CreditCost(20)`, `@Query(() => LeaderboardDTO)`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @Args | `period` | `string` | `'period', { defaultValue: '7d' }` |
| @Args | `sortBy` | `string` | `'sortBy', { defaultValue: 'revenue' }` |
| @Args | `limit` | `number` | `'limit', { type: () => Int, defaultValue: 10 }` |

### Query getCreatorTransactionHistory

- Source: `src/analytics/analytics.resolver.ts:67`
- Handler: `AnalyticsResolver.getCreatorTransactionHistory`
- Declared return: `Promise<TransactionHistoryDTO>`
- Decorators: `@CreditCost(10)`, `@Query(() => TransactionHistoryDTO)`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @Args | `userId` | `string` | `'userId'` |
| @Args | `cursor` | `string` | `'cursor', { nullable: true }` |
| @Args | `limit` | `number` | `'limit', { type: () => Int, defaultValue: 20 }` |

### Query getCreditBalance

- Source: `src/billing/billing.query.ts:76`
- Handler: `BillingQuery.getCreditBalance`
- Declared return: `Promise<CreditBalanceDTO>`
- Decorators: `@Query(() => CreditBalanceDTO)`, `@Authorize('user')`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @GetUserId | `userId` | `string` | `` |

### Query getCreditHistory

- Source: `src/billing/billing.query.ts:92`
- Handler: `BillingQuery.getCreditHistory`
- Declared return: `Promise<CreditLedgerDTO[]>`
- Decorators: `@Query(() => [CreditLedgerDTO])`, `@Authorize('user')`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @GetUserId | `userId` | `string` | `` |
| @Args | `limit` | `number` | `'limit', { type: () => Int, defaultValue: 20 }` |
| @Args | `offset` | `number` | `'offset', { type: () => Int, defaultValue: 0 }` |

### Query getExportStatus

- Source: `src/analytics/analytics.resolver.ts:196`
- Handler: `AnalyticsResolver.getExportStatus`
- Declared return: `Promise<BulkExportStatusDTO>`
- Decorators: `@Authorize('user')`, `@Query(() => BulkExportStatusDTO)`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @GetUserId | `userId` | `string` | `` |
| @Args | `exportId` | `string` | `'exportId'` |

### Query getFAQs

- Source: `src/user/user.query.ts:284`
- Handler: `UserQuery.getFAQs`
- Declared return: `Promise<QA[]>`
- Decorators: `@Query(() => [QA])`

Arguments/context bindings:

_None declared._

### Query getFAQsAdmin

- Source: `src/user/user.query.ts:295`
- Handler: `UserQuery.getFAQsAdmin`
- Declared return: `Promise<QA[]>`
- Decorators: `@Authorize('admin')`, `@Query(() => [QA])`

Arguments/context bindings:

_None declared._

### Query getFeatureFlags

- Source: `src/config/config.query.ts:31`
- Handler: `ConfigQuery.getFeatureFlags`
- Declared return: `Promise<FeatureFlagsDTO>`
- Decorators: `@Query(() => FeatureFlagsDTO)`

Arguments/context bindings:

_None declared._

### Query getFeed

- Source: `src/feed/feed.resolver.ts:10`
- Handler: `FeedResolver.getFeed`
- Declared return: `Promise<FeedResponseDTO>`
- Decorators: `@Authorize('user')`, `@Query(() => FeedResponseDTO)`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @GetUserId | `userId` | `string` | `` |
| @Args | `cursor` | `string` | `'cursor', { nullable: true }` |
| @Args | `limit` | `number` | `'limit', { type: () => Int, nullable: true, defaultValue: 20 }` |

### Query getFinalizedPayTokens

- Source: `src/listing/listing.query.ts:434`
- Handler: `ListingQuery.getFinalizedPayTokens`
- Declared return: `Promise<PayTokenResponseWithTotalDTO>`
- Decorators: `@Query(() => PayTokenResponseWithTotalDTO)`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @Args | `input` | `GetPayTokensDTO` | `'input'` |

### Query getHotListings

- Source: `src/analytics/analytics.resolver.ts:83`
- Handler: `AnalyticsResolver.getHotListings`
- Declared return: `Promise<TrendingListingsDTO>`
- Decorators: `@CreditCost(5)`, `@Query(() => TrendingListingsDTO)`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @Args | `limit` | `number` | `'limit', { type: () => Int, defaultValue: 10 }` |

### Query getListing

- Source: `src/listing/listing.query.ts:115`
- Handler: `ListingQuery.getListing`
- Declared return: `Promise<ListingDTO>`
- Decorators: `@ApplyTokenInfo`, `@Query(() => ListingDTO)`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @Args | `input` | `InputUUID` | `'input', { type: () => InputUUID }` |
| @GetUserId | `userId` | `string` | `` |

### Query getListingActivity

- Source: `src/activity/activity.query.ts:135`
- Handler: `ActivityQuery.getListingActivity`
- Declared return: `Promise<ListingActivityDTO>`
- Decorators: `@Authorize('user')`, `@Query(() => ListingActivityDTO)`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @Args | `input` | `InputUUID` | `'input'` |
| @GetUserId | `userId` | `string` | `` |

### Query getListingAnalytics

- Source: `src/analytics/analytics.resolver.ts:28`
- Handler: `AnalyticsResolver.getListingAnalytics`
- Declared return: `Promise<ListingAnalyticsDTO>`
- Decorators: `@CreditCost(5)`, `@Query(() => ListingAnalyticsDTO)`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @Args | `listingId` | `string` | `'listingId'` |

### Query getListingBid

- Source: `src/auction/auction.query.ts:26`
- Handler: `AuctionQuery.getListingBid`
- Declared return: `Promise<BidDTO>`
- Decorators: `@Authorize('user')`, `@Query(() => BidDTO)`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @Args | `input` | `InputUUID` | `'input'` |
| @GetUserId | `userId` | `string` | `` |

### Query getListingByName

- Source: `src/listing/listing.query.ts:79`
- Handler: `ListingQuery.getListingByName`
- Declared return: `Promise<ListingDTO>`
- Decorators: `@ApplyTokenInfo`, `@Query(() => ListingDTO)`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @Args | `input` | `InputName` | `'input', { type: () => InputName }` |
| @GetUserId | `userId` | `string` | `` |

### Query getListingBySlug

- Source: `src/listing/listing.query.ts:97`
- Handler: `ListingQuery.getListingBySlug`
- Declared return: `Promise<ListingDTO>`
- Decorators: `@ApplyTokenInfo`, `@Query(() => ListingDTO)`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @Args | `input` | `InputString` | `'input', { type: () => InputString }` |
| @GetUserId | `userId` | `string` | `` |

### Query getListingComments

- Source: `src/activity/activity.query.ts:192`
- Handler: `ActivityQuery.getListingComments`
- Declared return: `Promise<CommentReponseWithTotalDTO>`
- Decorators: `@ApplyTokenInfo`, `@Query(() => CommentReponseWithTotalDTO)`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @Args | `input` | `GetListingCommentsDTO` | `'input'` |
| @GetUserId | `userId` | `string` | `` |

### Query getListingCommentsCursor

- Source: `src/activity/activity.query.ts:203`
- Handler: `ActivityQuery.getListingCommentsCursor`
- Declared return: `Promise<PaginatedComments>`
- Decorators: `@ApplyTokenInfo`, `@Query(() => PaginatedComments)`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @Args | `listingId` | `string` | `'listingId'` |
| @Args | `first` | `number` | `'first', { type: () => Int }` |
| @Args | `after` | `string` | `'after', { nullable: true }` |
| @Args | `parentId` | `string` | `'parentId', { nullable: true }` |
| @GetUserId | `userId` | `string` | `` |

### Query getListingFile

- Source: `src/listing/listing.query.ts:186`
- Handler: `ListingQuery.getListingFile`
- Declared return: `Promise<ListingFileResponseDTO[]>`
- Decorators: `@Authorize('user')`, `@Query(() => [ListingFileResponseDTO])`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @Args | `input` | `InputUUID` | `'input'` |
| @GetUserId | `userId` | `string` | `` |

### Query getListingFlags

- Source: `src/listing/listing.query.ts:348`
- Handler: `ListingQuery.getListingFlags`
- Declared return: `Promise<ListingFlagDTO[]>`
- Decorators: `@Authorize('admin')`, `@Query(() => [ListingFlagDTO])`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @Args | `input` | `InputUUID` | `'input'` |

### Query getListingLikes

- Source: `src/activity/activity.query.ts:39`
- Handler: `ActivityQuery.getListingLikes`
- Declared return: `Promise<number>`
- Decorators: `@Query(() => Number)`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @Args | `input` | `InputUUID` | `'input'` |

### Query getListingMetadata

- Source: `src/listing/listing.query.ts:168`
- Handler: `ListingQuery.getListingMetadata`
- Declared return: `Promise<ListingMetadataDTO>`
- Decorators: `@Authorize('user')`, `@Query(() => ListingMetadataDTO)`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @Args | `input` | `InputUUID` | `'input', { type: () => InputUUID }` |
| @GetUserId | `userId` | `string` | `` |

### Query getListingOffers

- Source: `src/marketplace/marketplace.query.ts:41`
- Handler: `MarketplaceQuery.getListingOffers`
- Declared return: `Promise<OfferDTO[]>`
- Decorators: `@Authorize('user')`, `@Query(() => [OfferDTO])`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @GetUserId | `userId` | `string` | `` |
| @Args | `input` | `InputUUID` | `'input'` |

### Query getListingPriceHistory

- Source: `src/analytics/analytics.resolver.ts:36`
- Handler: `AnalyticsResolver.getListingPriceHistory`
- Declared return: `Promise<PriceHistoryDTO>`
- Decorators: `@CreditCost(10)`, `@Query(() => PriceHistoryDTO)`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @Args | `listingId` | `string` | `'listingId'` |
| @Args | `period` | `string` | `'period', { defaultValue: '30d' }` |

### Query getListingProcessLogs

- Source: `src/listing/listing.query.ts:358`
- Handler: `ListingQuery.getListingProcessLogs`
- Declared return: `Promise<ListingProcessLog[]>`
- Decorators: `@Authorize('admin')`, `@Query(() => [ListingProcessLog])`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @Args | `input` | `InputUUID` | `'input'` |

### Query getListingRank

- Source: `src/viral-score/viral-score.query.ts:21`
- Handler: `ViralScoreQuery.getListingRank`
- Declared return: `Promise<number>`
- Decorators: `@Authorize('user')`, `@CheckPermission(PermissionAction.VIEW_VIRAL_SCORE)`, `@Query(() => Number, { nullable: true })`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @Args | `input` | `InputUUID` | `'input'` |

### Query getListings

- Source: `src/listing/listing.query.ts:130`
- Handler: `ListingQuery.getListings`
- Declared return: `Promise<ListingDTO[]>`
- Decorators: `@ApplyTokenInfo`, `@Query(() => [ListingDTO])`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @Args | `input` | `InputArrayUUID` | `'input', { type: () => InputArrayUUID }` |
| @GetUserId | `userId` | `string` | `` |

### Query getListingTradeHistories

- Source: `src/activity/activity.query.ts:122`
- Handler: `ActivityQuery.getListingTradeHistories`
- Declared return: `Promise<TradeHistoryDTO[]>`
- Decorators: `@Authorize('user')`, `@CheckPermission(PermissionAction.VIEW_TX_HISTORY)`, `@Query(() => [TradeHistoryDTO])`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @Args | `input` | `InputUUID` | `'input'` |

### Query getListingTransactionHistory

- Source: `src/analytics/analytics.resolver.ts:45`
- Handler: `AnalyticsResolver.getListingTransactionHistory`
- Declared return: `Promise<TransactionHistoryDTO>`
- Decorators: `@CreditCost(10)`, `@Query(() => TransactionHistoryDTO)`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @Args | `listingId` | `string` | `'listingId'` |
| @Args | `cursor` | `string` | `'cursor', { nullable: true }` |
| @Args | `limit` | `number` | `'limit', { type: () => Int, defaultValue: 20 }` |

### Query getListingViewCount

- Source: `src/activity/activity.query.ts:69`
- Handler: `ActivityQuery.getListingViewCount`
- Declared return: `Promise<number>`
- Decorators: `@Query(() => Number)`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @Args | `input` | `InputUUID` | `'input'` |

### Query getMentions

- Source: `src/mention/mention.query.ts:13`
- Handler: `MentionQuery.getMentions`
- Declared return: `Promise<MentionDTO[]>`
- Decorators: `@Authorize('user')`, `@Query(() => [MentionDTO])`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @GetUserId | `userId` | `string` | `` |
| @Args | `limit` | `number` | `'limit', { type: () => Int, nullable: true, defaultValue: 20 }` |
| @Args | `offset` | `number` | `'offset', { type: () => Int, nullable: true, defaultValue: 0 }` |

### Query getMonthlyTotalPointEarned

- Source: `src/point/point.query.ts:44`
- Handler: `PointQuery.getMonthlyTotalPointEarned`
- Declared return: `Promise<number>`
- Decorators: `@Authorize('user')`, `@Query(() => Number)`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @GetUserId | `userId` | `string` | `` |

### Query getMyDownloadLicenses

- Source: `src/listing/listing.query.ts:259`
- Handler: `ListingQuery.getMyDownloadLicenses`
- Declared return: `Promise<Transaction[]>`
- Decorators: `@Authorize('user')`, `@Query(() => [Transaction])`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @GetUserId | `userId` | `string` | `` |

### Query getMyInteractionsTotal

- Source: `src/activity/activity.query.ts:182`
- Handler: `ActivityQuery.getMyInteractionsTotal`
- Declared return: `Promise<InteractionsTotalDTO>`
- Decorators: `@Authorize('user')`, `@Query(() => InteractionsTotalDTO)`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @GetUserId | `userId` | `string` | `` |

### Query getMySingleItemsTotal

- Source: `src/listing/listing.query.ts:211`
- Handler: `ListingQuery.getMySingleItemsTotal`
- Declared return: `Promise<Number>`
- Decorators: `@Authorize('user')`, `@Query(() => Number)`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @GetUserId | `userId` | `string` | `` |

### Query getNewSellers

- Source: `src/analytics/analytics.resolver.ts:117`
- Handler: `AnalyticsResolver.getNewSellers`
- Declared return: `Promise<LeaderboardEntryDTO[]>`
- Decorators: `@CreditCost(10)`, `@Query(() => [LeaderboardEntryDTO])`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @Args | `limit` | `number` | `'limit', { type: () => Int, defaultValue: 10 }` |

### Query getNotificationsCursor

- Source: `src/notifications/notifications.query.ts:29`
- Handler: `NotificationsQuery.getNotificationsCursor`
- Declared return: `Promise<PaginatedNotifications>`
- Decorators: `@Authorize('user')`, `@Query(() => PaginatedNotifications)`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @Args | `first` | `number` | `'first', { type: () => Int }` |
| @Args | `after` | `string` | `'after', { nullable: true }` |
| @Args | `includeViewed` | `boolean` | `'includeViewed', { nullable: true }` |
| @Args | `category` | `string` | `'category', { nullable: true }` |
| @GetUserId | `userId` | `string` | `` |

### Query getOffersTotal

- Source: `src/marketplace/marketplace.query.ts:55`
- Handler: `MarketplaceQuery.getOffersTotal`
- Declared return: `Promise<OffersTotalDTO>`
- Decorators: `@Authorize('user')`, `@Query(() => OffersTotalDTO)`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @GetUserId | `userId` | `string` | `` |

### Query getOutboxEntries

- Source: `src/resilience/outbox/outbox.resolver.ts:10`
- Handler: `OutboxResolver.getOutboxEntries`
- Declared return: `Promise<OutboxEntryDTO[]>`
- Decorators: `@Authorize('admin')`, `@Query(() => [OutboxEntryDTO])`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @Args | `status` | `string` | `'status', { nullable: true }` |
| @Args | `eventType` | `string` | `'eventType', { nullable: true }` |
| @Args | `limit` | `number` | `'limit', { type: () => Int, defaultValue: 20 }` |

### Query getPayTokens

- Source: `src/listing/listing.query.ts:413`
- Handler: `ListingQuery.getPayTokens`
- Declared return: `Promise<PayTokenResponseWithTotalDTO>`
- Decorators: `@Query(() => PayTokenResponseWithTotalDTO)`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @Args | `input` | `GetPayTokensDTO` | `'input'` |

### Query getPendingFiles

- Source: `src/listing/listing.query.ts:368`
- Handler: `ListingQuery.getPendingFiles`
- Declared return: `Promise<AssetDTO[]>`
- Decorators: `@Authorize('user')`, `@Query(() => [AssetDTO])`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @GetUserId | `userId` | `string` | `` |

### Query getPendingTransaction

- Source: `src/listing/listing.query.ts:300`
- Handler: `ListingQuery.getPendingTransaction`
- Declared return: `Promise<Transaction>`
- Decorators: `@Query(() => Transaction)`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @Args | `listingId` | `InputUUID` | `'input'` |

### Query getPlacedBids

- Source: `src/auction/auction.query.ts:37`
- Handler: `AuctionQuery.getPlacedBids`
- Declared return: `Promise<BidsResponseDTO>`
- Decorators: `@Authorize('user')`, `@Query(() => BidsResponseDTO)`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @GetUserId | `userId` | `string` | `` |
| @Args | `period` | `PeriodType` | `'period'` |

### Query getPlans

- Source: `src/billing/billing.query.ts:103`
- Handler: `BillingQuery.getPlans`
- Declared return: `Promise<PlanDTO[]>`
- Decorators: `@Query(() => [PlanDTO])`

Arguments/context bindings:

_None declared._

### Query getPointsBalance

- Source: `src/point/point.query.ts:54`
- Handler: `PointQuery.getPointsBalance`
- Declared return: `Promise<PointsBalanceDTO>`
- Decorators: `@Authorize('user')`, `@Query(() => PointsBalanceDTO)`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @GetUserId | `userId` | `string` | `` |

### Query getPointTypes

- Source: `src/point/point.query.ts:17`
- Handler: `PointQuery.getPointTypes`
- Declared return: `Promise<PointType[]>`
- Decorators: `@Authorize('admin')`, `@Query(() => [PointType])`

Arguments/context bindings:

_None declared._

### Query getPriceMovers

- Source: `src/analytics/analytics.resolver.ts:100`
- Handler: `AnalyticsResolver.getPriceMovers`
- Declared return: `Promise<TrendingListingsDTO>`
- Decorators: `@CreditCost(15)`, `@Query(() => TrendingListingsDTO)`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @Args | `direction` | `'up' \| 'down'` | `'direction', { defaultValue: 'up' }` |
| @Args | `limit` | `number` | `'limit', { type: () => Int, defaultValue: 10 }` |

### Query getProfileCounts

- Source: `src/user/user.query.ts:96`
- Handler: `UserQuery.getProfileCounts`
- Declared return: `Promise<ProfileCountsDTO>`
- Decorators: `@Authorize('user')`, `@Query(() => ProfileCountsDTO)`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @GetUserId | `userId` | `string` | `` |

### Query getProfileDashboard

- Source: `src/user/user.query.ts:104`
- Handler: `UserQuery.getProfileDashboard`
- Declared return: `Promise<ProfileDashboardDTO>`
- Decorators: `@ApplyTokenInfo`, `@Query(() => ProfileDashboardDTO)`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @Args | `input` | `InputUUID` | `'input'` |
| @GetUserId | `viewerId` | `string` | `` |

### Query getPurchaseStatus

- Source: `src/listing/listing.query.ts:474`
- Handler: `ListingQuery.getPurchaseStatus`
- Declared return: `Promise<PurchaseStatusDTO>`
- Decorators: `@Authorize('user')`, `@Query(() => PurchaseStatusDTO)`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @Args | `idempotencyKey` | `string` | `'idempotencyKey'` |
| @GetUserId | `userId` | `string` | `` |

### Query getQuestionTypes

- Source: `src/user/user.query.ts:301`
- Handler: `UserQuery.getQuestionTypes`
- Declared return: `Promise<QuestionType[]>`
- Decorators: `@Query(() => [QuestionType])`

Arguments/context bindings:

_None declared._

### Query getReceivedBids

- Source: `src/auction/auction.query.ts:15`
- Handler: `AuctionQuery.getReceivedBids`
- Declared return: `Promise<BidsResponseDTO>`
- Decorators: `@Authorize('user')`, `@Query(() => BidsResponseDTO)`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @GetUserId | `userId` | `string` | `` |
| @Args | `period` | `PeriodType` | `'period'` |

### Query getReceivedOffers

- Source: `src/marketplace/marketplace.query.ts:16`
- Handler: `MarketplaceQuery.getReceivedOffers`
- Declared return: `Promise<OffersResponseDTO>`
- Decorators: `@Authorize('user')`, `@Query(() => OffersResponseDTO)`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @GetUserId | `userId` | `string` | `` |
| @Args | `period` | `PeriodType` | `'period'` |

### Query getRepeatBuyerRate

- Source: `src/analytics/analytics.resolver.ts:158`
- Handler: `AnalyticsResolver.getRepeatBuyerRate`
- Declared return: `Promise<RepeatBuyerRateDTO>`
- Decorators: `@CreditCost(15)`, `@Query(() => RepeatBuyerRateDTO)`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @Args | `userId` | `string` | `'userId'` |

### Query getRewardTokenInfor

- Source: `src/user/user.query.ts:289`
- Handler: `UserQuery.getRewardTokenInfor`
- Declared return: `Promise<RewardTokenInforDTO>`
- Decorators: `@Authorize('admin')`, `@Query(() => RewardTokenInforDTO)`

Arguments/context bindings:

_None declared._

### Query getRewardTradeHistories

- Source: `src/point/point.query.ts:23`
- Handler: `PointQuery.getRewardTradeHistories`
- Declared return: `Promise<PointResponseDTO>`
- Decorators: `@Authorize('user')`, `@Query(() => PointResponseDTO)`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @GetUserId | `userId` | `string` | `` |
| @Args | `period` | `PeriodType` | `'period'` |

### Query getSentOffers

- Source: `src/marketplace/marketplace.query.ts:30`
- Handler: `MarketplaceQuery.getSentOffers`
- Declared return: `Promise<OffersResponseDTO>`
- Decorators: `@Authorize('user')`, `@Query(() => OffersResponseDTO)`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @GetUserId | `userId` | `string` | `` |
| @Args | `period` | `PeriodType` | `'period'` |

### Query getSingleAssetFlag

- Source: `src/listing/listing.query.ts:402`
- Handler: `ListingQuery.getSingleAssetFlag`
- Declared return: `Promise<AssetFlagDTO>`
- Decorators: `@Authorize('admin')`, `@Query(() => AssetFlagDTO)`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @Args | `input` | `InputUUID` | `'input'` |

### Query getSingleUser

- Source: `src/user/user.query.ts:218`
- Handler: `UserQuery.getSingleUser`
- Declared return: `Promise<AdminUser>`
- Decorators: `@Authorize('admin')`, `@Query(() => AdminUser)`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @Args | `input` | `InputUUID` | `'input'` |

### Query getSubscription

- Source: `src/billing/billing.query.ts:26`
- Handler: `BillingQuery.getSubscription`
- Declared return: `Promise<SubscriptionDTO>`
- Decorators: `@Query(() => SubscriptionDTO)`, `@Authorize('user')`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @GetUserId | `userId` | `string` | `` |

### Query getTierPricing

- Source: `src/billing/billing.query.ts:173`
- Handler: `BillingQuery.getTierPricing`
- Declared return: `Promise<TierPriceDTO[]>`
- Decorators: `@Query(() => [TierPriceDTO])`

Arguments/context bindings:

_None declared._

### Query getTopUpTiers

- Source: `src/billing/billing.query.ts:163`
- Handler: `BillingQuery.getTopUpTiers`
- Declared return: `Promise<TopUpTierDTO[]>`
- Decorators: `@Query(() => [TopUpTierDTO])`

Arguments/context bindings:

_None declared._

### Query getTotalShare

- Source: `src/activity/activity.query.ts:155`
- Handler: `ActivityQuery.getTotalShare`
- Declared return: `Promise<Number>`
- Decorators: `@Query(() => Number)`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @Args | `input` | `InputUUID` | `'input'` |

### Query getTransferSignature

- Source: `src/activity/activity.query.ts:162`
- Handler: `ActivityQuery.getTransferSignature`
- Declared return: `Promise<string>`
- Decorators: `@Authorize('user')`, `@Query(() => String)`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @GetUserId | `userId` | `string` | `` |
| @Args | `message` | `SignMessageDTO` | `'input'` |

### Query getTrendingListings

- Source: `src/analytics/analytics.resolver.ts:91`
- Handler: `AnalyticsResolver.getTrendingListings`
- Declared return: `Promise<TrendingListingsDTO>`
- Decorators: `@CreditCost(20)`, `@Query(() => TrendingListingsDTO)`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @Args | `period` | `string` | `'period', { defaultValue: '24h' }` |
| @Args | `limit` | `number` | `'limit', { type: () => Int, defaultValue: 10 }` |

### Query getUserAccountDetails

- Source: `src/user/user.query.ts:153`
- Handler: `UserQuery.getUserAccountDetails`
- Declared return: `Promise<PrivateUser>`
- Decorators: `@Authorize('user')`, `@Query(() => PrivateUser)`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @Args | `input` | `WalletAddressDTO` | `'input'` |

### Query getUserFollowerAccounts

- Source: `src/activity/activity.query.ts:94`
- Handler: `ActivityQuery.getUserFollowerAccounts`
- Declared return: `Promise<PublicUser[]>`
- Decorators: `@ApplyTokenInfo`, `@Query(() => [PublicUser])`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @Args | `input` | `InputUUID` | `'input'` |
| @GetUserId | `userId` | `string` | `` |

### Query getUserFollowingAccounts

- Source: `src/activity/activity.query.ts:108`
- Handler: `ActivityQuery.getUserFollowingAccounts`
- Declared return: `Promise<PublicUser[]>`
- Decorators: `@ApplyTokenInfo`, `@Query(() => [PublicUser])`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @Args | `input` | `InputUUID` | `'input'` |
| @GetUserId | `userId` | `string` | `` |

### Query getUserGrandReferrals

- Source: `src/user/user.query.ts:76`
- Handler: `UserQuery.getUserGrandReferrals`
- Declared return: `Promise<ReferralDTO[]>`
- Decorators: `@Authorize('user')`, `@Query(() => [ReferralDTO])`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @GetUserId | `userId` | `string` | `` |

### Query getUserInteractionsForListings

- Source: `src/search/search.resolver.ts:147`
- Handler: `SearchResolver.getUserInteractionsForListings`
- Declared return: `Promise<ListingInteractionDTO[]>`
- Decorators: `@Authorize('user')`, `@Query(() => [ListingInteractionDTO])`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @Args | `input` | `GetUserInteractionsDTO` | `'input'` |
| @GetUserId | `userId` | `string` | `` |

### Query getUserInteractionsTotal

- Source: `src/activity/activity.query.ts:173`
- Handler: `ActivityQuery.getUserInteractionsTotal`
- Declared return: `Promise<InteractionsTotalDTO>`
- Decorators: `@Query(() => InteractionsTotalDTO)`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @Args | `input` | `InputUUID` | `'input'` |

### Query getUserInviteTokens

- Source: `src/user/user.query.ts:183`
- Handler: `UserQuery.getUserInviteTokens`
- Declared return: `Promise<RegistrationToken[]>`
- Decorators: `@Authorize('user')`, `@Query(() => [RegistrationToken])`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @GetUserId | `userId` | `string` | `` |

### Query getUserNetworkInfo

- Source: `src/activity/activity.query.ts:76`
- Handler: `ActivityQuery.getUserNetworkInfo`
- Declared return: `Promise<UserNetworkDTO>`
- Decorators: `@Query(() => UserNetworkDTO)`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @Args | `input` | `WalletAddressDTO` | `'input'` |

### Query getUserNetworkInfoById

- Source: `src/activity/activity.query.ts:85`
- Handler: `ActivityQuery.getUserNetworkInfoById`
- Declared return: `Promise<UserNetworkDTO>`
- Decorators: `@Query(() => UserNetworkDTO)`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @Args | `input` | `InputUUID` | `'input'` |

### Query getUserNotificationSettings

- Source: `src/user/user.query.ts:244`
- Handler: `UserQuery.getUserNotificationSettings`
- Declared return: `Promise<NotificationSetting[]>`
- Decorators: `@Authorize('user')`, `@Query(() => [NotificationSetting])`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @GetUserId | `userId` | `string` | `` |

### Query getUserPayTokens

- Source: `src/listing/listing.query.ts:422`
- Handler: `ListingQuery.getUserPayTokens`
- Declared return: `Promise<PayTokenResponseWithTotalDTO>`
- Decorators: `@Authorize('user')`, `@Query(() => PayTokenResponseWithTotalDTO)`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @Args | `input` | `GetPayTokensDTO` | `'input'` |
| @GetUserId | `userId` | `string` | `` |

### Query getUserPayTokensTotal

- Source: `src/listing/listing.query.ts:466`
- Handler: `ListingQuery.getUserPayTokensTotal`
- Declared return: `Promise<number>`
- Decorators: `@Authorize('user')`, `@Query(() => Number)`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @GetUserId | `userId` | `string` | `` |

### Query getUserProfile

- Source: `src/user/user.query.ts:42`
- Handler: `UserQuery.getUserProfile`
- Declared return: `Promise<PrivateUser>`
- Decorators: `@Authorize('user')`, `@Query(() => PrivateUser)`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @GetUserId | `userId` | `string` | `` |

### Query getUserProfileByUserName

- Source: `src/user/user.query.ts:235`
- Handler: `UserQuery.getUserProfileByUserName`
- Declared return: `Promise<PublicUser>`
- Decorators: `@Query(() => PublicUser)`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @Args | `input` | `InputName` | `'input'` |

### Query getUserProfileByWalletAddress

- Source: `src/user/user.query.ts:226`
- Handler: `UserQuery.getUserProfileByWalletAddress`
- Declared return: `Promise<PublicUser>`
- Decorators: `@Query(() => PublicUser)`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @Args | `input` | `WalletAddressDTO` | `'input'` |

### Query getUserReferralCode

- Source: `src/user/user.query.ts:66`
- Handler: `UserQuery.getUserReferralCode`
- Declared return: `Promise<ReferralResponseDTO>`
- Decorators: `@Authorize('user')`, `@Query(() => ReferralResponseDTO)`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @GetUserId | `userId` | `string` | `` |

### Query getUserReferrals

- Source: `src/user/user.query.ts:54`
- Handler: `UserQuery.getUserReferrals`
- Declared return: `Promise<ReferralDTO[]>`
- Decorators: `@Authorize('user')`, `@Query(() => [ReferralDTO])`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @GetUserId | `userId` | `string` | `` |

### Query getUserReferralsTotal

- Source: `src/user/user.query.ts:90`
- Handler: `UserQuery.getUserReferralsTotal`
- Declared return: `Promise<number>`
- Decorators: `@Authorize('user')`, `@Query(() => Number)`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @GetUserId | `userId` | `string` | `` |

### Query getUserSingleItemsTotal

- Source: `src/listing/listing.query.ts:219`
- Handler: `ListingQuery.getUserSingleItemsTotal`
- Declared return: `Promise<Number>`
- Decorators: `@Query(() => Number)`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @Args | `input` | `InputUUID` | `'input'` |

### Query getUserViralScore

- Source: `src/viral-score/viral-score.query.ts:28`
- Handler: `ViralScoreQuery.getUserViralScore`
- Declared return: `Promise<number>`
- Decorators: `@Authorize('user')`, `@CheckPermission(PermissionAction.VIEW_VIRAL_SCORE)`, `@Query(() => Number, { nullable: true })`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @Args | `input` | `InputUUID` | `'input'` |

### Query getUserWaitlist

- Source: `src/user/user.query.ts:175`
- Handler: `UserQuery.getUserWaitlist`
- Declared return: `Promise<Waitlist[]>`
- Decorators: `@Authorize('user')`, `@Query(() => [Waitlist])`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @GetUserId | `userId` | `string` | `` |

### Query getValidationString

- Source: `src/user/user.query.ts:275`
- Handler: `UserQuery.getValidationString`
- Declared return: `Promise<ValidationStringResponseDTO>`
- Decorators: `@Authorize('user')`, `@Query(() => ValidationStringResponseDTO)`

Arguments/context bindings:

_None declared._

### Query getViralScore

- Source: `src/viral-score/viral-score.query.ts:13`
- Handler: `ViralScoreQuery.getViralScore`
- Declared return: `Promise<number | null>`
- Decorators: `@Authorize('user')`, `@CheckPermission(PermissionAction.VIEW_VIRAL_SCORE)`, `@Query(() => Number, { nullable: true })`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @Args | `input` | `InputUUID` | `'input'` |

### Query isUserFollowing

- Source: `src/activity/activity.query.ts:58`
- Handler: `ActivityQuery.isUserFollowing`
- Declared return: `Promise<boolean>`
- Decorators: `@Authorize('user')`, `@Query(() => Boolean)`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @Args | `from` | `InputUUID` | `'from'` |
| @Args | `to` | `InputUUID` | `'to'` |

### Query listingFolders

- Source: `src/folder/resolvers/folder.query.ts:132`
- Handler: `FolderQuery.listingFolders`
- Declared return: `Promise<Folder[]>`
- Decorators: `@Authorize('user')`, `@Query(() => [Folder])`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @GetUserId | `userId` | `string` | `` |
| @Args | `listingId` | `string` | `'listingId'` |

### Query myFeedHistory

- Source: `src/user-feed-queue/resolvers/user-feed-queue.query.ts:22`
- Handler: `UserFeedQueueQueryResolver.myFeedHistory`
- Declared return: `Promise<UserFeedHistoryPageDto>`
- Decorators: `@Query(() => UserFeedHistoryPageDto)`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @GetUserId | `userId` | `string` | `` |
| @Args | `limit` | `number` | `'limit', { type: () => Int, nullable: true }` |
| @Args | `cursor` | `string` | `'cursor', { nullable: true }` |

### Query myFeedQueue

- Source: `src/user-feed-queue/resolvers/user-feed-queue.query.ts:14`
- Handler: `UserFeedQueueQueryResolver.myFeedQueue`
- Declared return: `Promise<UserFeedQueueDto>`
- Decorators: `@Query(() => UserFeedQueueDto)`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @GetUserId | `userId` | `string` | `` |

### Query myFolderEngagement
_Task 4.9 — myFolderEngagement Single SELECT returning the caller's active engagement state on a folder as three booleans. Used by the frontend to render Liked / Save / Follow toggle UI. Does not enforce engageability here; any authenticated user can query the state of their own engagement on any folder ID (attempting to engage with a private folder they don't own will fail in FolderEngagementService.assertEngageable)._

- Source: `src/folder/resolvers/folder.query.ts:151`
- Handler: `FolderQuery.myFolderEngagement`
- Declared return: `Promise<FolderEngagementState>`
- Decorators: `@Authorize('user')`, `@Query(() => FolderEngagementState)`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @GetUserId | `userId` | `string` | `` |
| @Args | `folderId` | `string` | `'folderId'` |

### Query myFolders

- Source: `src/folder/resolvers/folder.query.ts:47`
- Handler: `FolderQuery.myFolders`
- Declared return: `Promise<Folder[]>`
- Decorators: `@Authorize('user')`, `@Query(() => [Folder])`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @GetUserId | `userId` | `string` | `` |
| @Args | `type` | `FolderType` | `'type', { type: () => FolderType, nullable: true }` |

### Query mySavedFolders

- Source: `src/folder/resolvers/folder.query.ts:57`
- Handler: `FolderQuery.mySavedFolders`
- Declared return: `Promise<Folder[]>`
- Decorators: `@Authorize('user')`, `@Query(() => [Folder])`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @GetUserId | `userId` | `string` | `` |

### Query ownerPublicFolders

- Source: `src/folder/resolvers/folder.query.ts:123`
- Handler: `FolderQuery.ownerPublicFolders`
- Declared return: `Promise<Folder[]>`
- Decorators: `@ApplyTokenInfo`, `@Query(() => [Folder])`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @Args | `userId` | `string` | `'userId'` |
| @GetUserId | `viewerId` | `string` | `` |

### Query ownerPublicPlaylists

- Source: `src/folder/resolvers/folder.query.ts:114`
- Handler: `FolderQuery.ownerPublicPlaylists`
- Declared return: `Promise<Folder[]>`
- Decorators: `@ApplyTokenInfo`, `@Query(() => [Folder])`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @Args | `userId` | `string` | `'userId'` |
| @GetUserId | `viewerId` | `string` | `` |

### Query ownerPublicPortfolios

- Source: `src/folder/resolvers/folder.query.ts:105`
- Handler: `FolderQuery.ownerPublicPortfolios`
- Declared return: `Promise<Folder[]>`
- Decorators: `@ApplyTokenInfo`, `@Query(() => [Folder])`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @Args | `userId` | `string` | `'userId'` |
| @GetUserId | `viewerId` | `string` | `` |

### Query payTokenExists

- Source: `src/listing/listing.query.ts:458`
- Handler: `ListingQuery.payTokenExists`
- Declared return: `Promise<boolean>`
- Decorators: `@Authorize('user')`, `@Query(() => Boolean)`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @Args | `input` | `InputETH` | `'input'` |

### Query previewListingVisibilityChange

- Source: `src/listing/listing.query.ts:483`
- Handler: `ListingQuery.previewListingVisibilityChange`
- Declared return: `Promise<VisibilityChangePreviewDTO>`
- Decorators: `@Authorize('user')`, `@Query(() => VisibilityChangePreviewDTO)`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @GetUserId | `userId` | `string` | `` |
| @Args | `listingId` | `string` | `'listingId'` |

### Query searchFolders

- Source: `src/search/search.resolver.ts:172`
- Handler: `SearchResolver.searchFolders`
- Declared return: `Promise<PaginatedFoldersSearchResult>`
- Decorators: `@Query(() => PaginatedFoldersSearchResult)`, `@Throttle({ default: { limit: 60, ttl: 60_000 } })`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @Args | `input` | `SearchFoldersInput` | `'input'` |

### Query searchNames

- Source: `src/listing/listing.query.ts:70`
- Handler: `ListingQuery.searchNames`
- Declared return: `Promise<SearchNamesResponseDTO>`
- Decorators: `@Query(() => SearchNamesResponseDTO)`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @Args | `input` | `SearchNamesDTO` | `'input'` |

### Query searchUsers

- Source: `src/search/search.resolver.ts:159`
- Handler: `SearchResolver.searchUsers`
- Declared return: `Promise<PublicUser[]>`
- Decorators: `@Query(() => [PublicUser])`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @Args | `query` | `string` | `'query'` |
| @Args | `limit` | `number` | `'limit', { type: () => Int, nullable: true, defaultValue: 10 }` |

### Query sendReferralEmail

- Source: `src/user/user.query.ts:142`
- Handler: `UserQuery.sendReferralEmail`
- Declared return: `Promise<boolean>`
- Decorators: `@Authorize('user')`, `@Query(() => Boolean)`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @Args | `email` | `string` | `'email'` |
| @GetUserId | `userId` | `string` | `` |

### Query validateInviteCode

- Source: `src/user/user.query.ts:193`
- Handler: `UserQuery.validateInviteCode`
- Declared return: `Promise<boolean>`
- Decorators: `@Query(() => Boolean)`

Arguments/context bindings:

| Source | Name | Type | Decorator args |
|---|---|---|---|
| @Args | `token` | `string` | `'token'` |
