python -m bin.infer \
  --tasks "
    - class: DecodeText" \
  --model_dir cs221_both_output_vocab \
  --checkpoint_path "cs221_both_output_vocab/model.ckpt-1000" \
  --input_pipeline "
    class: ParallelTextInputPipeline
    params:
      source_files:
        - Desktop/CS221_EXP/CS221_EXP/both_dataset/english_unparsed_dev_both.BPE.L1" \
  > Desktop/CS221_EXP/predictions/both_1000.txt
python -m bin.infer \
  --tasks "
    - class: DecodeText" \
  --model_dir cs221_both_output_vocab \
  --checkpoint_path "cs221_both_output_vocab/model.ckpt-2000" \
  --input_pipeline "
    class: ParallelTextInputPipeline
    params:
      source_files:
        - Desktop/CS221_EXP/CS221_EXP/both_dataset/english_unparsed_dev_both.BPE.L1" \
  > Desktop/CS221_EXP/predictions/both_2000.txt
python -m bin.infer \
  --tasks "
    - class: DecodeText" \
  --model_dir cs221_both_output_vocab \
  --checkpoint_path "cs221_both_output_vocab/model.ckpt-3000" \
  --input_pipeline "
    class: ParallelTextInputPipeline
    params:
      source_files:
        - Desktop/CS221_EXP/CS221_EXP/both_dataset/english_unparsed_dev_both.BPE.L1" \
  > Desktop/CS221_EXP/predictions/both_3000.txt
python -m bin.infer \
  --tasks "
    - class: DecodeText" \
  --model_dir cs221_both_output_vocab \
  --checkpoint_path "cs221_both_output_vocab/model.ckpt-4000" \
  --input_pipeline "
    class: ParallelTextInputPipeline
    params:
      source_files:
        - Desktop/CS221_EXP/CS221_EXP/both_dataset/english_unparsed_dev_both.BPE.L1" \
  > Desktop/CS221_EXP/predictions/both_4000.txt
python -m bin.infer \
  --tasks "
    - class: DecodeText" \
  --model_dir cs221_both_output_vocab \
  --checkpoint_path "cs221_both_output_vocab/model.ckpt-5000" \
  --input_pipeline "
    class: ParallelTextInputPipeline
    params:
      source_files:
        - Desktop/CS221_EXP/CS221_EXP/both_dataset/english_unparsed_dev_both.BPE.L1" \
  > Desktop/CS221_EXP/predictions/both_5000.txt
python -m bin.infer \
  --tasks "
    - class: DecodeText" \
  --model_dir cs221_both_output_vocab \
  --checkpoint_path "cs221_both_output_vocab/model.ckpt-6000" \
  --input_pipeline "
    class: ParallelTextInputPipeline
    params:
      source_files:
        - Desktop/CS221_EXP/CS221_EXP/both_dataset/english_unparsed_dev_both.BPE.L1" \
  > Desktop/CS221_EXP/predictions/both_6000.txt
python -m bin.infer \
  --tasks "
    - class: DecodeText" \
  --model_dir cs221_both_output_vocab \
  --checkpoint_path "cs221_both_output_vocab/model.ckpt-7000" \
  --input_pipeline "
    class: ParallelTextInputPipeline
    params:
      source_files:
        - Desktop/CS221_EXP/CS221_EXP/both_dataset/english_unparsed_dev_both.BPE.L1" \
  > Desktop/CS221_EXP/predictions/both_7000.txt
python -m bin.infer \
  --tasks "
    - class: DecodeText" \
  --model_dir cs221_both_output_vocab \
  --checkpoint_path "cs221_both_output_vocab/model.ckpt-8000" \
  --input_pipeline "
    class: ParallelTextInputPipeline
    params:
      source_files:
        - Desktop/CS221_EXP/CS221_EXP/both_dataset/english_unparsed_dev_both.BPE.L1" \
  > Desktop/CS221_EXP/predictions/both_8000.txt
python -m bin.infer \
  --tasks "
    - class: DecodeText" \
  --model_dir cs221_both_output_vocab \
  --checkpoint_path "cs221_both_output_vocab/model.ckpt-9000" \
  --input_pipeline "
    class: ParallelTextInputPipeline
    params:
      source_files:
        - Desktop/CS221_EXP/CS221_EXP/both_dataset/english_unparsed_dev_both.BPE.L1" \
  > Desktop/CS221_EXP/predictions/both_9000.txt
python -m bin.infer \
  --tasks "
    - class: DecodeText" \
  --model_dir cs221_both_output_vocab \
  --checkpoint_path "cs221_both_output_vocab/model.ckpt-10000" \
  --input_pipeline "
    class: ParallelTextInputPipeline
    params:
      source_files:
        - Desktop/CS221_EXP/CS221_EXP/both_dataset/english_unparsed_dev_both.BPE.L1" \
  > Desktop/CS221_EXP/predictions/both_10000.txt
python -m bin.infer \
  --tasks "
    - class: DecodeText" \
  --model_dir cs221_both_output_vocab \
  --checkpoint_path "cs221_both_output_vocab/model.ckpt-11000" \
  --input_pipeline "
    class: ParallelTextInputPipeline
    params:
      source_files:
        - Desktop/CS221_EXP/CS221_EXP/both_dataset/english_unparsed_dev_both.BPE.L1" \
  > Desktop/CS221_EXP/predictions/both_11000.txt
python -m bin.infer \
  --tasks "
    - class: DecodeText" \
  --model_dir cs221_both_output_vocab \
  --checkpoint_path "cs221_both_output_vocab/model.ckpt-12000" \
  --input_pipeline "
    class: ParallelTextInputPipeline
    params:
      source_files:
        - Desktop/CS221_EXP/CS221_EXP/both_dataset/english_unparsed_dev_both.BPE.L1" \
  > Desktop/CS221_EXP/predictions/both_12000.txt
python -m bin.infer \
  --tasks "
    - class: DecodeText" \
  --model_dir cs221_both_output_vocab \
  --checkpoint_path "cs221_both_output_vocab/model.ckpt-13000" \
  --input_pipeline "
    class: ParallelTextInputPipeline
    params:
      source_files:
        - Desktop/CS221_EXP/CS221_EXP/both_dataset/english_unparsed_dev_both.BPE.L1" \
  > Desktop/CS221_EXP/predictions/both_13000.txt
python -m bin.infer \
  --tasks "
    - class: DecodeText" \
  --model_dir cs221_both_output_vocab \
  --checkpoint_path "cs221_both_output_vocab/model.ckpt-14000" \
  --input_pipeline "
    class: ParallelTextInputPipeline
    params:
      source_files:
        - Desktop/CS221_EXP/CS221_EXP/both_dataset/english_unparsed_dev_both.BPE.L1" \
  > Desktop/CS221_EXP/predictions/both_14000.txt
python -m bin.infer \
  --tasks "
    - class: DecodeText" \
  --model_dir cs221_both_output_vocab \
  --checkpoint_path "cs221_both_output_vocab/model.ckpt-15000" \
  --input_pipeline "
    class: ParallelTextInputPipeline
    params:
      source_files:
        - Desktop/CS221_EXP/CS221_EXP/both_dataset/english_unparsed_dev_both.BPE.L1" \
  > Desktop/CS221_EXP/predictions/both_15000.txt
python -m bin.infer \
  --tasks "
    - class: DecodeText" \
  --model_dir cs221_both_output_vocab \
  --checkpoint_path "cs221_both_output_vocab/model.ckpt-16000" \
  --input_pipeline "
    class: ParallelTextInputPipeline
    params:
      source_files:
        - Desktop/CS221_EXP/CS221_EXP/both_dataset/english_unparsed_dev_both.BPE.L1" \
  > Desktop/CS221_EXP/predictions/both_16000.txt
python -m bin.infer \
  --tasks "
    - class: DecodeText" \
  --model_dir cs221_both_output_vocab \
  --checkpoint_path "cs221_both_output_vocab/model.ckpt-17000" \
  --input_pipeline "
    class: ParallelTextInputPipeline
    params:
      source_files:
        - Desktop/CS221_EXP/CS221_EXP/both_dataset/english_unparsed_dev_both.BPE.L1" \
  > Desktop/CS221_EXP/predictions/both_17000.txt
python -m bin.infer \
  --tasks "
    - class: DecodeText" \
  --model_dir cs221_both_output_vocab \
  --checkpoint_path "cs221_both_output_vocab/model.ckpt-18000" \
  --input_pipeline "
    class: ParallelTextInputPipeline
    params:
      source_files:
        - Desktop/CS221_EXP/CS221_EXP/both_dataset/english_unparsed_dev_both.BPE.L1" \
  > Desktop/CS221_EXP/predictions/both_18000.txt
python -m bin.infer \
  --tasks "
    - class: DecodeText" \
  --model_dir cs221_both_output_vocab \
  --checkpoint_path "cs221_both_output_vocab/model.ckpt-19000" \
  --input_pipeline "
    class: ParallelTextInputPipeline
    params:
      source_files:
        - Desktop/CS221_EXP/CS221_EXP/both_dataset/english_unparsed_dev_both.BPE.L1" \
  > Desktop/CS221_EXP/predictions/both_19000.txt
python -m bin.infer \
  --tasks "
    - class: DecodeText" \
  --model_dir cs221_both_output_vocab \
  --checkpoint_path "cs221_both_output_vocab/model.ckpt-20000" \
  --input_pipeline "
    class: ParallelTextInputPipeline
    params:
      source_files:
        - Desktop/CS221_EXP/CS221_EXP/both_dataset/english_unparsed_dev_both.BPE.L1" \
  > Desktop/CS221_EXP/predictions/both_20000.txt
python -m bin.infer \
  --tasks "
    - class: DecodeText" \
  --model_dir cs221_both_output_vocab \
  --checkpoint_path "cs221_both_output_vocab/model.ckpt-21000" \
  --input_pipeline "
    class: ParallelTextInputPipeline
    params:
      source_files:
        - Desktop/CS221_EXP/CS221_EXP/both_dataset/english_unparsed_dev_both.BPE.L1" \
  > Desktop/CS221_EXP/predictions/both_21000.txt
python -m bin.infer \
  --tasks "
    - class: DecodeText" \
  --model_dir cs221_both_output_vocab \
  --checkpoint_path "cs221_both_output_vocab/model.ckpt-22000" \
  --input_pipeline "
    class: ParallelTextInputPipeline
    params:
      source_files:
        - Desktop/CS221_EXP/CS221_EXP/both_dataset/english_unparsed_dev_both.BPE.L1" \
  > Desktop/CS221_EXP/predictions/both_22000.txt
python -m bin.infer \
  --tasks "
    - class: DecodeText" \
  --model_dir cs221_both_output_vocab \
  --checkpoint_path "cs221_both_output_vocab/model.ckpt-23000" \
  --input_pipeline "
    class: ParallelTextInputPipeline
    params:
      source_files:
        - Desktop/CS221_EXP/CS221_EXP/both_dataset/english_unparsed_dev_both.BPE.L1" \
  > Desktop/CS221_EXP/predictions/both_23000.txt
python -m bin.infer \
  --tasks "
    - class: DecodeText" \
  --model_dir cs221_both_output_vocab \
  --checkpoint_path "cs221_both_output_vocab/model.ckpt-24000" \
  --input_pipeline "
    class: ParallelTextInputPipeline
    params:
      source_files:
        - Desktop/CS221_EXP/CS221_EXP/both_dataset/english_unparsed_dev_both.BPE.L1" \
  > Desktop/CS221_EXP/predictions/both_24000.txt
python -m bin.infer \
  --tasks "
    - class: DecodeText" \
  --model_dir cs221_both_output_vocab \
  --checkpoint_path "cs221_both_output_vocab/model.ckpt-25000" \
  --input_pipeline "
    class: ParallelTextInputPipeline
    params:
      source_files:
        - Desktop/CS221_EXP/CS221_EXP/both_dataset/english_unparsed_dev_both.BPE.L1" \
  > Desktop/CS221_EXP/predictions/both_25000.txt
python -m bin.infer \
  --tasks "
    - class: DecodeText" \
  --model_dir cs221_both_output_vocab \
  --checkpoint_path "cs221_both_output_vocab/model.ckpt-26000" \
  --input_pipeline "
    class: ParallelTextInputPipeline
    params:
      source_files:
        - Desktop/CS221_EXP/CS221_EXP/both_dataset/english_unparsed_dev_both.BPE.L1" \
  > Desktop/CS221_EXP/predictions/both_26000.txt
python -m bin.infer \
  --tasks "
    - class: DecodeText" \
  --model_dir cs221_both_output_vocab \
  --checkpoint_path "cs221_both_output_vocab/model.ckpt-27000" \
  --input_pipeline "
    class: ParallelTextInputPipeline
    params:
      source_files:
        - Desktop/CS221_EXP/CS221_EXP/both_dataset/english_unparsed_dev_both.BPE.L1" \
  > Desktop/CS221_EXP/predictions/both_27000.txt
python -m bin.infer \
  --tasks "
    - class: DecodeText" \
  --model_dir cs221_both_output_vocab \
  --checkpoint_path "cs221_both_output_vocab/model.ckpt-28000" \
  --input_pipeline "
    class: ParallelTextInputPipeline
    params:
      source_files:
        - Desktop/CS221_EXP/CS221_EXP/both_dataset/english_unparsed_dev_both.BPE.L1" \
  > Desktop/CS221_EXP/predictions/both_28000.txt
python -m bin.infer \
  --tasks "
    - class: DecodeText" \
  --model_dir cs221_both_output_vocab \
  --checkpoint_path "cs221_both_output_vocab/model.ckpt-29000" \
  --input_pipeline "
    class: ParallelTextInputPipeline
    params:
      source_files:
        - Desktop/CS221_EXP/CS221_EXP/both_dataset/english_unparsed_dev_both.BPE.L1" \
  > Desktop/CS221_EXP/predictions/both_29000.txt
python -m bin.infer \
  --tasks "
    - class: DecodeText" \
  --model_dir cs221_both_output_vocab \
  --checkpoint_path "cs221_both_output_vocab/model.ckpt-30000" \
  --input_pipeline "
    class: ParallelTextInputPipeline
    params:
      source_files:
        - Desktop/CS221_EXP/CS221_EXP/both_dataset/english_unparsed_dev_both.BPE.L1" \
  > Desktop/CS221_EXP/predictions/both_30000.txt
python -m bin.infer \
  --tasks "
    - class: DecodeText" \
  --model_dir cs221_both_output_vocab \
  --checkpoint_path "cs221_both_output_vocab/model.ckpt-31000" \
  --input_pipeline "
    class: ParallelTextInputPipeline
    params:
      source_files:
        - Desktop/CS221_EXP/CS221_EXP/both_dataset/english_unparsed_dev_both.BPE.L1" \
  > Desktop/CS221_EXP/predictions/both_31000.txt
python -m bin.infer \
  --tasks "
    - class: DecodeText" \
  --model_dir cs221_both_output_vocab \
  --checkpoint_path "cs221_both_output_vocab/model.ckpt-32000" \
  --input_pipeline "
    class: ParallelTextInputPipeline
    params:
      source_files:
        - Desktop/CS221_EXP/CS221_EXP/both_dataset/english_unparsed_dev_both.BPE.L1" \
  > Desktop/CS221_EXP/predictions/both_32000.txt
python -m bin.infer \
  --tasks "
    - class: DecodeText" \
  --model_dir cs221_both_output_vocab \
  --checkpoint_path "cs221_both_output_vocab/model.ckpt-33000" \
  --input_pipeline "
    class: ParallelTextInputPipeline
    params:
      source_files:
        - Desktop/CS221_EXP/CS221_EXP/both_dataset/english_unparsed_dev_both.BPE.L1" \
  > Desktop/CS221_EXP/predictions/both_33000.txt
python -m bin.infer \
  --tasks "
    - class: DecodeText" \
  --model_dir cs221_both_output_vocab \
  --checkpoint_path "cs221_both_output_vocab/model.ckpt-34000" \
  --input_pipeline "
    class: ParallelTextInputPipeline
    params:
      source_files:
        - Desktop/CS221_EXP/CS221_EXP/both_dataset/english_unparsed_dev_both.BPE.L1" \
  > Desktop/CS221_EXP/predictions/both_34000.txt
python -m bin.infer \
  --tasks "
    - class: DecodeText" \
  --model_dir cs221_both_output_vocab \
  --checkpoint_path "cs221_both_output_vocab/model.ckpt-35000" \
  --input_pipeline "
    class: ParallelTextInputPipeline
    params:
      source_files:
        - Desktop/CS221_EXP/CS221_EXP/both_dataset/english_unparsed_dev_both.BPE.L1" \
  > Desktop/CS221_EXP/predictions/both_35000.txt