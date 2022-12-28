from ocrbot.helpers.decorators import send_typing_action
from telegram import Update
from telegram.ext import CallbackContext

@send_typing_action
def start(update:Update,context:CallbackContext):
    """Send a message when the command /start is issued."""
    first=update.effective_user.first_name
    update.message.reply_text('السلام عليكم يا '+str(first)+' \n\nأنا بوت أقوم بتحويل الصور إلى نص . فقط أرسل لي الصور هنا . \n\n لبقية البوتات هنا https://t.me/ibnAlQyyim/1120 \n\n لدعم استمرار المشروع هنا http://paypal.me/kelectronic89 ',quote=True)
