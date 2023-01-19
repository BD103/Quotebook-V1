CREATE MIGRATION m1qpszciihylz3nny6rqlyq536hr4k5h5rx27xnepluiaxpcj4zt2q
    ONTO m1hquddbsflymk5h333cf3dwsrwu5mkliyachdrkgx2x6srxkq7xbq
{
  ALTER TYPE default::Quote {
      ALTER PROPERTY date {
          SET default := (std::datetime_of_statement());
      };
  };
};
