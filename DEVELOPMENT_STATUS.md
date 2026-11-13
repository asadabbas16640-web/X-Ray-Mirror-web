# X-Ray Mirror — Verified Development Status (2026-11-13)

This repository preserves the original working head-and-hand X-Ray Mirror application in `xray_mirror_https_pages.zip`. The deployed index is extracted from that ZIP and receives navigation links to separate research modules. The original reference HTML has SHA-256 `b5e12cd0755ac0976e655c4f9ac914c2a7a6b54474455d66549cbdfa6511dfb0`; CI rejects changes to that reference.

## Implemented source modules (not clinical validation)

- `medical-review.html`: original PNG/JPEG/WebP image display with manual review markers; never modifies source pixels.
- `dicom-review.html`: limited uncompressed monochrome single-frame DICOM viewer.
- `ct-series.html`: axial, coronal, and sagittal reslicing of strictly compatible uncompressed CT stacks.
- `ct-3d.html`: coarse thresholded voxel surface from actual CT pixel data. **Not** clinically accurate bone segmentation.
- `anatomy-3d.html`: loads a user-provided anatomical GLB file and allows visibility/opacity control. **No full-body anatomical asset is bundled.**
- `full-body-lab.html`: live pose landmark tracking only. **Does not display full-body bone meshes or register anatomy to the body.**

## Tests

GitHub Actions runs `scripts/check-deployment.py` before publishing. It verifies:
- Original source reference checksum.
- Required HTML files and local relative links.
- Unique HTML IDs.
- JavaScript syntax using Node, skipping JSON and binary script payloads.

A local source check of the original 2.7 MB HTML confirmed that its only executable inline module passes `node --check`. The source check does **not** establish real browser functionality, live camera tracking, medical-image correctness, or clinical diagnostic performance.

## Not complete

1. Licensed, detailed head-to-toe anatomical meshes and their provenance.
2. Full-body anatomical rigging with reliable joint registration and calibration.
3. Robust clinical-grade DICOM support (compressed formats, enhanced multiframe, complete series geometry, hanging protocols).
4. Validated CT bone segmentation and clinically meaningful 3D reconstruction.
5. Clinically validated fracture detection with independent evaluation.
6. Clinically validated neuromuscular, spinal-level, or nerve compression analysis.
7. End-to-end device testing on desktop and Samsung S24 Ultra.

No code in this repository is validated for clinical diagnosis or treatment. The webcam cannot see actual fractures. X-ray images do not directly measure nerve compression or muscle pressure.

## Next engineering gates

- Obtain or authorize an appropriately licensed full-body anatomical model and verify its structure and rig.
- Implement rig-to-pose landmark mapping and calibration with quantitative alignment tests.
- Validate DICOM and CT reconstructions using reference datasets and established medical imaging software.
- Select and independently evaluate fracture-specific AI models using licensed, de-identified labeled imaging data.
- Complete clinical, security, privacy, and applicable regulatory review before patient use.
