from h2o_wave import main, app, Q, ui, copy_expando, site
from utils.predictor import predict

async def init(q: Q):
    if not q.client.app_initialized:
        q.client.app_initialized = True
    q.page.drop()

    q.page["title"] = ui.header_card(
        box="1 1 8 1",
        title="Depression Detection",
        subtitle="Detect depression level using texts...",
        icon="AddNotes",
        icon_color="White",
    )

async def get_inputs(q: Q):
    q.page['main'] = ui.form_card(box="1 2 8 5", items=[
        ui.text_xl('Enter your text input for the prediction:'),
        ui.textbox(name="input_text",
                   label='',
                   value=q.app.input_text,
                   multiline=True),
        ui.separator(),
        ui.buttons([ui.button(name="generate_text", label='Predict', primary=True),
                    ])
    ])

async def show_results(q: Q):
    q.page['main'] = ui.form_card(box="1 2 4 5", items=[
        ui.text_xl("Input Text:"),
        ui.separator(),
        ui.text(q.app.input_text),
        ui.separator(),
        ui.buttons([ui.button(name="get_inputs", label='Try Again!', primary=True),
                    ])
    ])
    result, tips = predict(q.app.input_text)
    q.app.prediction = result
    q.app.tips = tips
    q.page['visualization'] = ui.form_card(box="5 2 4 5", items=[
        ui.text_xl("Predicted Results"),
        ui.separator(''),
        ui.text(q.app.prediction),
        ui.separator(''),
        ui.text(q.app.tips)
    ])
    

@app("/")
async def serve(q: Q):
    await init(q)
    if q.args.generate_text:
        copy_expando(q.args, q.app)
        await show_results(q)
    else:
        await get_inputs(q)
    await q.page.save()