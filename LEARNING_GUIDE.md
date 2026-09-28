# ShelfMatch — learning guide

## What it does

Find products with text and visual constraints. The intended user is catalog users. Browser controls → validated Flask API → project analysis/workflow → results and export.

## Run and demonstrate

Follow the README installation block, then: Search blue striped fabric, choose a visual reference, vary the blend weight, and filter to tile. Inspect images alongside text/visual component scores.

## Important files

- `app.py` — local HTTP interface and request/error handling.
- `core.py` — project-specific logic.
- `tests/` — regression and correctness checks.
- `reports/` — recorded outputs and verification evidence.

## Three engineering decisions

1. Represent catalog text with TF-IDF and images with explicit color histograms plus directional texture descriptors.
2. Combine normalized similarity scores with a visible text/image weight.
3. Use original procedural swatches and deterministic IDs so the entire multimodal example is reproducible.

## Five interview questions

1. **What makes the search multimodal?** The final ranking combines TF-IDF text similarity with image color and texture similarities. Both text and visual input can change the order of results.

2. **Is this a pretrained vision-language model?** No. It is an interpretable feature baseline over an original sixteen-swatch catalog. It should not be presented as CLIP or semantic scene understanding.

3. **Why expose the modality weight?** A user can see how prioritizing appearance versus description changes a result. The tradeoff is explicit and useful for explaining ranking behavior.

4. **What are the dataset boundaries?** The fabric/tile swatches are procedurally generated, not real retailer inventory. Image queries use catalog examples; arbitrary uploaded-product recognition is not implemented.

5. **How would you measure better retrieval?** Create labeled query–relevant-product pairs, hold some out, and evaluate ranking metrics such as recall at k. Visual plausibility alone is insufficient evidence of improvement.

## Independent exercise

Implement image upload with dimension limits and compare its descriptor against the same catalog.

Write down the expected behavior before editing. Add a meaningful regression check, run the existing suite, and describe what changed in your own words.

## Contribution and resume guidance

The implementation was developed with substantial AI assistance under Abhijith Viswanathan's direction. The verified contribution is the working artifact and the learning work actually completed, not invented employment or adoption.

Suggested factual bullet after personally validating the demo:

- Implemented weighted text-and-image product ranking using TF-IDF, color and texture features over sixteen original procedural swatches; verified twelve checks.

Use [VERIFICATION.md](VERIFICATION.md) to add only measured numbers. Do not claim production traffic, users, savings, upstream acceptance or cloud deployment without corresponding evidence.
