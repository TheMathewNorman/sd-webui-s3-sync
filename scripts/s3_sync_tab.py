import modules.scripts as scripts
import gradio as gr
import os

from modules import script_callbacks


def on_ui_tabs():
    with gr.Blocks(analytics_enabled=False) as ui_component:
        syncBtn = gr.Button(value="Sync Now")
        with gr.Accordion("Settings"):
            bucketTxt = gr.Textbox(label="S3 Bucket", value="s3://bucket-name")
            folderTxt = gr.Textbox(label="S3 Folder", value="output")
            with gr.Row():
                optionRadio = gr.Radio(["sync", "copy", "move"], label="Action", info="S3 command?"),
            syncBtn = gr.Button(value="Sync")

            
        return [(ui_component, "S3 Sync", "s3_sync_tab")]

script_callbacks.on_ui_tabs(on_ui_tabs)
