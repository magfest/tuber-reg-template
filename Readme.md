# Tuber Registration Template

This is a companion to [Tuber](https://github.com/magfest/tuber).

Tuber is meant to run as a multi-year system, and does not support any form of per-event theming or customization. This repo shows how to spin up a separate registration frontend for Tuber so that you can add theming and a customized registration workflow.

## Why is this separate from Tuber?

Events often have strong opinions about what is shown to attendees, how different registration options are presented or combined, what questions to ask, etc. What doesn't change from one event to another is payment processing and storing a ledger of transactions. Thus Tuber implements a simple ledger and external systems (like this one) implement a cart and form workflow.

This repo will be maintained alongside Tuber as a super simple registration form with bare-bones theming and cart functionality. When starting an event simply fork this repo, make it pretty, then shut it down and don't worry about maintaining it after. All your data is safe in the main Tuber instance and presented there in a theme agnostic format.

Additionally, by running as a separate service the frontend can scale to many simultaneous registrations and the Tuber backend server can run a single API call per attendee.