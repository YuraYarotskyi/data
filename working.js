function usr_control(type, username, mail, password)
{

    const spawner = require('child_process').spawn;
    const python_process = spawner('python', ['./python.py', type, username, mail, password]);

    python_process.stdout.on('data', (data) => {
        data.toString();
    }); 
}

usr_control("login", "randomusr", "random@mail.com", "randompass")
