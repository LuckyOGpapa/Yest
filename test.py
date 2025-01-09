from pyrogram import Client

async def main():
    api_id = "28073859"
    api_hash = "7ba18e1a9922df6797a5610c59b2381a"
    
    app = Client("my_account", api_id=api_id, api_hash=api_hash)

    print("Logging in...")
    async with app:
        session_string = await app.export_session_string()
        print("Session string generated!")
        
        await app.send_message("me", f"Here is your session string:\n\n`{session_string}`")
        print("Session string saved to Saved Messages!")

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())