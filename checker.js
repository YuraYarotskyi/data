const stream = require('node:stream'); 
const spawner = require('child_process').spawn;
const {Duplex} = stream.Duplex;

async function usr_control(type, username, mail, password)
{
    const [command, args] = ['python', ['./python.py', type, username, mail, password]];
    const { stdout, stderr } = spawner(command, args);
    const { readable } = Duplex.toWeb(stdout);
    const data = await new Response(readable).text();

    return data;
}

console.log(usr_control("register", "fsfsdf", "dsfsdfsd", "fdsfsdfsd"))


// module.exports = usr_control;