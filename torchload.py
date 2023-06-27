import torch
import os

# Specify the path to the GPT model file
model_path = os.environ.get('MODEL_PATH')

# Load the GPT model
model = torch.load(model_path, map_location=torch.device('cpu'))

# Inspect the model
print(model)