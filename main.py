from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
TOKEN: Final = 'Telegram Bot Token'
BOT_USERNAME: Final = '@DevsKlaporeBot'
#BotCommands
async def start_command(update: Update, Context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Hello Im DevsBot And Im Created By DevsKlapore Nice To Meet You!')

async def help_command(update: Update, Context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Hello Im Devs Bot Type What You Want And Ill Respond To It!')

async def custom_command(update: Update, Context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('This Is A Blank Code!')
#BotHandleResponses
def handle_response(text: str)-> str:
    processed: str = text.lower()
    processed: str = text.upper()
    if 'Hello' in processed:
        return 'Hi!'
    if 'How Are You' in processed:
        return 'Im Good!'
    if 'I Love You' in processed:
        return 'I Love You Too!'
    return 'I Dont Understand What You Wrote'

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type
    text: str = update.message.text

    print(f'User ({update.message.chat.id}) in {message_type}: "{text}"')

    if message_type == 'group':
        if BOT_USERNAME in text:
            new_text: str = text.replace(BOT_USERNAME, '').strip()
            response: str = handle_response(new_text)
        else:
            return
    else:
        response: str = handle_response(text)
    print('Bot:', response)
    await update.message.reply_text(response)

async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
        print(f'Update {update} caused error {context.error}')

if __name__ == '__main__':
   print('Starting Bot..')
   app = Application.builder().token(TOKEN).build()

   #Commands
   app.add_handler(CommandHandler('start', start_command))
   app.add_handler(CommandHandler('help', help_command))
   app.add_handler(CommandHandler('custom', custom_command))

   #messages
   app.add_error_handler(error)

   #Polling
   print('Polling...')
   app.run_polling(poll_interval=3)
