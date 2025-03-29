from finn.builder.build_dataflow import build_dataflow_cfg
from finn.builder.build_dataflow import build_dataflow

# Create a configuration object
cfg = build_dataflow_cfg

# Set the model file
cfg.model = "model.onnx"  # Path to your ONNX file

# Set the output directory
cfg.output_dir = "./output"

# Target the Artix-7 FPGA
cfg.target_device = "xc7a100t"  # Artix-7 FPGA

# Build the dataflow model
build_dataflow(cfg)
