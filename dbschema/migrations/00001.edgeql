CREATE MIGRATION m1hquddbsflymk5h333cf3dwsrwu5mkliyachdrkgx2x6srxkq7xbq
    ONTO initial
{
  CREATE FUTURE nonrecursive_access_policies;
  CREATE TYPE default::Quote {
      CREATE PROPERTY date -> std::datetime;
      CREATE PROPERTY quotee -> std::str {
          CREATE CONSTRAINT std::max_len_value(50);
      };
      CREATE REQUIRED PROPERTY text -> std::str {
          CREATE CONSTRAINT std::max_len_value(200);
      };
  };
};
