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

1. **What problem does this project solve, and what is its unit of work?** Explain find products with text and visual constraints, identify catalog users as the audience, and trace one concrete example through the files above. Use the demonstration output rather than hypothetical impact.
2. **Why did you choose the first design decision?** Represent catalog text with TF-IDF and images with explicit color histograms plus directional texture descriptors. Show the corresponding implementation and a test that would fail if that property were removed.
3. **How do you protect correctness when inputs or execution change?** Combine normalized similarity scores with a visible text/image weight. Explain the relevant invalid-input or edge-case test and distinguish a checked property from an untested assumption.
4. **How do you make results inspectable and reproducible?** Use original procedural swatches and deterministic IDs so the entire multimodal example is reproducible. Point to actual outputs and recorded commands. Explain why a successful example is weaker evidence than a tested boundary or independently reconciled total.
5. **What would you improve before real deployment or real-data use?** An engineered multimodal retrieval baseline, not a pretrained neural vision-language system. Sixteen synthetic material swatches; visual queries select a catalog reference instead of accepting arbitrary uploads. Similarities are not probabilities. Choose one limitation, describe the missing evidence, and propose a measurable acceptance check rather than promising production readiness.

## Independent exercise

Implement image upload with dimension limits and compare its descriptor against the same catalog.

Write down the expected behavior before editing. Add a meaningful regression check, run the existing suite, and describe what changed in your own words.

## Contribution and resume guidance

The implementation was developed with substantial AI assistance under Abhijith Viswanathan's direction. The verified contribution is the working artifact and the learning work actually completed, not invented employment or adoption.

Suggested factual bullet after personally validating the demo:

- Implemented and validated find products with text and visual constraints using Pillow · scikit-learn · Flask, with text and image descriptor retrieval and documented correctness checks and limitations.

Use [VERIFICATION.md](VERIFICATION.md) to add only measured numbers. Do not claim production traffic, users, savings, upstream acceptance or cloud deployment without corresponding evidence.
