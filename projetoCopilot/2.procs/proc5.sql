select 'alter user ' || login_name || ' set LOGIN_NAME = ''' || email || ''';',
       'ALTER USER ' || LOGIN_NAME || ' SET TYPE = ''person'';'

from snowflake.account_usage.users
where deleted_on is null
and login_name not ilike 'SF_%'
and login_name not ilike 'x_%'
and login_name <> upper(email)
and disabled = FALSE;