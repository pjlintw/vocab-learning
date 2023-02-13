
MODEL=GPT2
DATA=/local/pinjie/m2d2/md_data/sample_10k/valid.txt

python validate_on_multiple_files.py \
	--model_id $MODEL \
	--list_of_valid_paths valid_files.txt \
	--output_file eval.out
