db.createUser({
  user: 'admin',
  pwd: 'admin',
  roles: [{ role: 'root', db: 'admin' }]
});

db = db.getSiblingDB('portfolio');

db.createCollection('users');

db.users.insertMany([
  {
    username: 'testuser',
    password: 'scrypt:32768:8:1$3ZG8PYJfQ8ToOFx0$1be6dcae74479bea1c6d218bc2eb1fefaa7d323f079449ed3d800457f17d21d543f184599a68a35b008f1689eacddfb3162a6f10b3c5007c1da5d1614aff1abf'
  }
]);
