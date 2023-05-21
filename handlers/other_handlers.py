from aiogram import Router, types
from aiogram.types import FSInputFile
from path import ticket_bel_dict, ticket_dict, voise_ticket


router: Router = Router()



@router.message()
async def ticket(message: types.Message):
    if message.text.lower() in ticket_dict:
        media =  FSInputFile(path=ticket_dict[message.text.lower()])
        await message.answer_document(document=media)
    if message.text.lower() in ticket_bel_dict:
        media =  FSInputFile(path=ticket_bel_dict[message.text.lower()])
        await message.answer_document(document=media)
    if message.text.lower() in voise_ticket:
        media = FSInputFile(path=voise_ticket[message.text.lower()])
        await message.answer_audio(audio=media)