#!/bin/zsh

current_path=$(pwd)

cd /Users/you/src/mlx-examples

echo "Fine tuning..."
python -m mlx_lm.lora --config "$current_path/config/lora_config.yaml"

echo "Merging ..."
python -m mlx_lm.fuse \
    --model /Users/you/src/llm_demo/outputs/zypt_7B \
    --adapter-path /Users/you/models/lora \
    --save-path /Users/you/models/fuse

echo Done