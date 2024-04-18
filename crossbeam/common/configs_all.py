from ml_collections import config_dict


def get_config():
  """Get config_dict."""
  cfg_dict = dict(
    # from crossbeam.common.config
    seed=1,
    data_folder=config_dict.FieldReference(None, field_type=str),
    save_dir=config_dict.FieldReference(None, field_type=str),
    load_model=config_dict.FieldReference(None, field_type=str),
    do_test=False,
    json_results_file=config_dict.FieldReference(None, field_type=str),
    batch_size=32,
    embed_dim=512,
    n_para_dataload=0,
    decoder_rnn_layers=3,
    grad_clip=5.0,
    train_steps=10000,
    eval_every=1000,
    log_every=1,
    lr=0.0001,
    beam_size=4,
    great_transformer=False,
    gpu=-1,
    port='29500',
    gpu_list=config_dict.FieldReference(None, field_type=str),
    num_proc=1,
    # from crossbeam.datasets.data_gen_flags
    data_gen_seed=1,
    shard_start_index=0,
    domain='tuple',
    output_file=config_dict.FieldReference(None, field_type=str),
    num_datagen_proc=1,
    shard_size=100000,
    num_tasks=1000,
    num_searches=100,
    data_gen_timeout=60,
    num_examples=2,
    min_num_examples=2,
    max_num_examples=4,
    min_num_inputs=1,
    max_num_inputs=3,
    min_task_weight=3,
    max_task_weight=10,
    skip_probability=0.0,
    lambda_skip_probability=0.0,
    lambda_fraction=config_dict.FieldReference(None, field_type=float),
    verbose=False,
    # from crossbeam.experiment.exp_common
    pooling='mean',
    step_score_func='mlp',
    arg_selector='lstm',
    use_op_specific_lstm=False,
    train_data_glob=config_dict.FieldReference(None, field_type=str),
    test_data_glob=config_dict.FieldReference(None, field_type=str),
    use_ur=True,
    score_normed=True,
    type_masking=True,
    grad_accumulate=1,
    max_search_weight=12,
    num_valid=-1,
    timeout=60.0,
    max_values_explored=config_dict.FieldReference(None, field_type=int),
    io_encoder='char',
    value_encoder='char',
    encode_weight=False,
    static_weight=False,
    # from crossbeam.experiment.run_baseline_synthesizer
    eval_set_pkl=config_dict.FieldReference(None, field_type=str),
    num_eval_tasks=5,
    # from crossbeam.experiment.run_crossbeam
    model_type='char',
    stochastic_beam=False,
    random_beam=False,
    schedule_type='uniform',
    steps_per_curr_stage=0,
    restarts_timeout=None,
    temperature=1.0,
    synthetic_test_tasks=False,
  )
  config = config_dict.ConfigDict(initial_dictionary=cfg_dict)
  return config