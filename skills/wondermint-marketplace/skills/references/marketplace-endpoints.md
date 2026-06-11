# Marketplace Endpoint Reference

Use this only after reading [Marketplace Router](../marketplace.md). This is an
endpoint inventory, not permission to perform every listed action. Before
calling any mutating endpoint, confirm the approval gate, error handling, and
verification steps in the matching marketplace flow.

## Browse And Detail

Read-only discovery endpoints. Existing discovery guidance may use these.

```http
GET /api/v1/agents/marketplace
GET /api/v1/agents/marketplace/:id
GET /api/v1/agents/marketplace/folders
GET /api/v1/agents/marketplace/users/:username
GET /api/v1/agents/marketplace/users/search
```

## Direct Purchase And Access

Financial actions require explicit user approval before the request. Poll
purchase status with the same idempotency key returned or used by the buy
request.

```http
POST /api/v1/agents/listings/:id/buy
GET /api/v1/agents/listings/:id/purchase-status
GET /api/v1/agents/purchases
GET /api/v1/agents/listings/:id/access
GET /api/v1/agents/listings/:id/download
GET /api/v1/agents/listings/:id/metadata
```

## Publish And Unpublish

Publishing and unpublishing are user-visible listing mutations. Confirm the
listing, price terms, visibility, and permanence before calling.

```http
POST /api/v1/agents/listings/:id/publish
POST /api/v1/agents/listings/:id/unpublish
PATCH /api/v1/agents/listings/:id/price
GET /api/v1/agents/listings/:id/estimate
```

## PayPal Setup

PayPal setup is required by some marketplace purchase or publishing flows. The
callback endpoints are redirect targets, not normal agent calls. Treat this as
marketplace payment setup only; do not use it for account-linking, payouts,
settlements, or earnings.

```http
POST /api/v1/agents/setup/paypal
POST /api/v1/agents/setup/paypal/complete
POST /api/v1/agents/setup/paypal/seller
GET /api/v1/agents/setup/paypal/callback/:state
GET /api/v1/agents/setup/paypal/kyc-callback
```
