# Samsung S24 Ultra camera acceptance test

Test URL: https://asadabbas16640-web.github.io/X-Ray-Mirror-web/full-body-lab.html

After the GitHub Pages deployment completes, open the page in Chrome on the S24 Ultra over HTTPS.

1. Tap **Start camera** and approve camera permission.
2. Stand back far enough for head, hips, knees, and feet to fit in frame.
3. Confirm the live video shows your body, with named tracking labels moving with the correct joints.
4. Tap **Run device checks**. Confirm `cameraActive` is true, `trackerReady` is true, and `framesWithPose` increases after several seconds.
5. Tap **Switch front/back camera**. Verify the view changes. Tap **Run device checks** again and inspect `actualFacing`. The phone may ignore facing requests if the browser cannot provide that camera.
6. Tap **Copy test report** and share its text with the developer. The report includes browser information and camera settings but does not contain video or photos.
7. Tap **Stop** and verify the camera indicator turns off.

Pass criteria: video renders without stretching, body labels align with the visible person, front/back switching works, the report shows a live camera and detected pose frames, and stopping releases the camera.

If `framesWithPose` remains zero, improve lighting and include your full body. If it remains zero, share the test report and a screenshot without private information.

**Known limitation:** Landmark tracking is not anatomical X-ray imaging; user-provided GLB is only previewed, not rigged to live pose. Clinical fracture and nerve diagnostics remain unimplemented.
