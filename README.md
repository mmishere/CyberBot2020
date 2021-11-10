## CyberBot2020 in action
![Character ideas](https://user-images.githubusercontent.com/70784810/121263137-cf097180-c87a-11eb-8240-01368db9ad01.png)
![Print stats](https://user-images.githubusercontent.com/70784810/121263203-e6e0f580-c87a-11eb-9347-c84a789f79c1.png)
A Discord bot to help with Cyberpunk 2020 and Cyberpunk Red.

It provides character ideas and lets you store your characters with the bot. Characters are uniquely identified by user first, then name. So two different accounts can both have the character Johnny Silverhand, but any given account can only have one instance of him.

## Adding CyberBot2020 to your server
Simply go to this link and add it to your server from there: https://discord.com/api/oauth2/authorize?client_id=849350543129968641&permissions=67584&scope=bot

## Using the bot
Use !! to call on the bot.

`!!help`: Help page.

`!!idea`: Gives you a character idea.

`!!make2020`: Add a Cyberpunk 2020 character to the database as such: Character_Name Character_Role INT REF TECH COOL ATTR LUCK MA BODY EMP. Prints the character's information once they're in the database.

`!!makered`: Like `!!make2020`, but with Cyberpunk Red characters. Add them to the database as such: Character_Name Character_Role INT REF DEX TECH COOL WILL LUCK MOVE BODY EMP. Prints the character's information once they're in the database.

`!!print2020`: Prints the information of an existing Cyberpunk 2020 character complete with derived stats in an easy-to-read format. Remember to add the character to the database using `!!make2020` first.

`!!printred`: The same as `!!print2020`, but for Cyberpunk Red characters. Remember to add the character with `!!makered` first.

`!!del2020`: Deletes an existing Cyberpunk 2020 character from the database. If they don't exist, a message indicating this will be sent.

`!!delred`: Same as `!!del2020`, but for Cyberpunk Red characters.

## License
This bot has the GNU General Public License. This project is open-source, and if you want to use it for yourself, then that also has to be open-source. For more details, see the license text.
