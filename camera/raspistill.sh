#!/usr/bin/env sh

/opt/vc/bin/raspistill -w 800 -h 600 -n -o - \
  | /usr/bin/convert \
      -font Fira-Sans-SemiBold \
      -pointsize 50 \
      -gravity south \
      -annotate 0 "$(date)" \
      -fill white \
      -- - - \
  | /usr/bin/curl \
      -X PUT \
      -H 'Content-Type: image/jpeg' \
      --data-binary @- \
      https://example.com/path/to/endpoint

