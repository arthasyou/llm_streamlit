#!/bin/zsh

cd /Users/you/src/mlx-examples

echo "Fine tuning..."
python -m mlx_lm.lora --config ../config/lora_config.yaml

echo "Merging ..."
python -m mlx_lm.lora --config ../config/fuse_config.yaml

echo Done