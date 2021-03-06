(* Delegates the messages to SpaxeBot *)

on encode(str)
  set safeStr to do shell script "echo " & quoted form of str & " | openssl base64 -e"
  return safeStr
end encode

on decode(safeStr)
  set str to do shell script "echo " & quoted form of safeStr & " | openssl base64 -d"
  return str
end decode

on SpaxeBot(str)
  set safeStr to encode(str)
  set SpaxeBotSays to do shell script "python /Users/spaxe/Dropbox/Projects/Scripts/Messages/com.apple.iChat/SpaxeBot.py " & quoted form of safeStr
  return SpaxeBotSays as string
end SpaxeBot

using terms from application "Messages"

  -- Because Messages insists on returning something, we need to turn it around
  -- so the bot can reply *after* the outgoing message.
  on message sent theMessage for theChat
    set SpaxeBotSays to SpaxeBot(theMessage)
    if length of SpaxeBotSays = 0 then
      return theMessage
    else
      send theMessage to theChat
      return SpaxeBotSays
    end if
  end message sent

  on message received theMessage for theChat
    send SpaxeBot(theMessage) to theChat
  end message received

  on chat room message received theMessage for theChat
    -- send SpaxeBot(theMessage) to theChat
  end chat room message received

  on active chat message received theMessage for theChat
    -- send SpaxeBot(theMessage) to theChat
  end active chat message received

  -- The following are unused but need to be defined to avoid an error

  on addressed message received theMessage from theBuddy for theChat with eventDescription

  end addressed message received

  on addressed chat room message received with eventDescription

  end addressed chat room message received

  on received text invitation theText from theBuddy for theChat with eventDescription

  end received text invitation

  on received audio invitation theText from theBuddy for theChat with eventDescription

  end received audio invitation

  on received video invitation theText from theBuddy for theChat with eventDescription

  end received video invitation

  on received remote screen sharing invitation from theBuddy for theChat with eventDescription

  end received remote screen sharing invitation

  on received local screen sharing invitation from theBuddy for theChat with eventDescription

  end received local screen sharing invitation

  on received file transfer invitation theFileTransfer with eventDescription

  end received file transfer invitation

  on buddy authorization requested with eventDescription

  end buddy authorization requested

  on av chat started with eventDescription

  end av chat started

  on av chat ended with eventDescription

  end av chat ended

  on login finished for theService with eventDescription

  end login finished

  on logout finished for theService with eventDescription

  end logout finished

  on buddy became available with eventDescription

  end buddy became available

  on buddy became unavailable with eventDescription
    try
      # do nothing
    on error errMsg
      display dialog "ERROR: " & errMsg
    end try
  end buddy became unavailable

  on completed file transfer with eventDescription

  end completed file transfer
end using terms from