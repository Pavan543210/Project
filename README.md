---
license: apache-2.0
base_model: distilbert-base-uncased
tags:
- generated_from_keras_callback
model-index:
- name: pavanch121/distilbert-base-uncased-finetuned-ner
  results: []
datasets:
- wnut_17
metrics:
- accuracy
- f1
pipeline_tag: token-classification
---

<!-- This model card has been generated automatically according to the information Keras had access to. You should
probably proofread and complete it, then remove this comment. -->

# pavanch121/distilbert-base-uncased-finetuned-ner

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on an unknown dataset.
It achieves the following results on the evaluation set:
- Train Loss: 0.1260
- Validation Loss: 0.3615
- Train Precision: 0.5297
- Train Recall: 0.3331
- Train F1: 0.4090
- Train Accuracy: 0.9222
- Epoch: 2

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- optimizer: {'name': 'AdamWeightDecay', 'learning_rate': {'module': 'keras.optimizers.schedules', 'class_name': 'PolynomialDecay', 'config': {'initial_learning_rate': 2e-05, 'decay_steps': 636, 'end_learning_rate': 0.0, 'power': 1.0, 'cycle': False, 'name': None}, 'registered_name': None}, 'decay': 0.0, 'beta_1': 0.9, 'beta_2': 0.999, 'epsilon': 1e-08, 'amsgrad': False, 'weight_decay_rate': 0.01}
- training_precision: float32

### Training results

| Train Loss | Validation Loss | Train Precision | Train Recall | Train F1 | Train Accuracy | Epoch |
|:----------:|:---------------:|:---------------:|:------------:|:--------:|:--------------:|:-----:|
| 0.2876     | 0.4266          | 0.4194          | 0.0103       | 0.0202   | 0.8971         | 0     |
| 0.1648     | 0.3597          | 0.5281          | 0.3362       | 0.4109   | 0.9210         | 1     |
| 0.1260     | 0.3615          | 0.5297          | 0.3331       | 0.4090   | 0.9222         | 2     |


### Framework versions

- Transformers 4.40.1
- TensorFlow 2.15.0
- Datasets 2.19.0
- Tokenizers 0.19.1