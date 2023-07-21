const { Telegraf } = require('telegraf');

const bot = new Telegraf('YOUR_BOT_TOKEN');

bot.command('start', (ctx) => {
  ctx.reply('Готовлю колы!');
});

bot.on('text', (ctx) => {
  try {
    const messageText = ctx.message.text;

    if (messageText === 'На хуй' || messageText === 'Посадить на хуй') {
      ctx.reply('Себя нахуй посади');
    }

    if (messageText === 'Посадить на кол' || messageText === 'На кол') {
      const replyUserId = ctx.message.reply_to_message.from.id;
      const replyUserName = ctx.message.reply_to_message.from.username;
      const currentUserUsername = ctx.message.from.username;

      if (replyUserName === 'Indra_0000') {
        ctx.reply('Индру на кол нельзя!!!');
      } else if (replyUserName === 'zarinsiki') {
        ctx.reply('Любимую Каночку нельзя!!!!');
      } else {
        ctx.reply(`${replyUserName} был посажен на кол ${currentUserUsername}`);
      }
    }
  } catch (error) {
    ctx.reply('Ответь на сообщение, гений');
  }
});

bot.launch();
