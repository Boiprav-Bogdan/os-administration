#!/bin/bash

file_count=$(find /etc -type f | wc -l)

echo "Files in /etc: $file_count"
