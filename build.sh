#!/bin/bash

mkdir -p docs &&
    python3 compilehtml.py &&
    cp src/web/styles/* docs/ &&
    cp src/web/img/* docs/ &&
    echo "done"
