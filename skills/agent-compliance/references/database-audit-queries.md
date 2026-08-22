# Database Audit Queries and Checks

Read this reference only for a live or supplied Supabase or Postgres access-control audit. Adapt queries to the actual version, schemas, permissions, and tool surface. Run read-only inspection before any proposed migration.

## Policies and RLS

Inspect table RLS state and policy definitions through the available metadata tools or equivalent catalog queries. For policy shape:

```sql
select schemaname, tablename, policyname, permissive, roles, cmd, qual, with_check
from pg_policies
where schemaname = any (/* scoped schemas */)
order by schemaname, tablename, cmd, policyname;
```

Check whether exposed tables have RLS enabled, whether applicable policies exist, and whether multiple permissive policies broaden access through `OR`. Remember:

- no applicable policy after RLS enablement produces default-deny behaviour for ordinary access;
- `USING` controls existing-row visibility and affected rows;
- `WITH CHECK` controls new row values for insert or update; and
- table owners and roles with `BYPASSRLS` normally bypass row security.

Verify these details against the current [PostgreSQL row-security documentation](https://www.postgresql.org/docs/current/ddl-rowsecurity.html) and [CREATE POLICY reference](https://www.postgresql.org/docs/current/sql-createpolicy.html).

## Roles, grants, and defaults

Inspect only the roles and objects needed for the scoped access paths. Useful evidence may include:

```sql
select grantee, table_schema, table_name, privilege_type
from information_schema.role_table_grants
where table_schema = any (/* scoped schemas */)
order by table_schema, table_name, grantee, privilege_type;
```

Also inspect role membership, login, superuser and `BYPASSRLS` attributes, sequence and function grants, schema usage, object ownership, and default privileges where they can create future exposure. Do not print passwords, connection strings, secrets, or unrelated role details.

## Privileged functions and views

For flagged functions:

```sql
select
  p.oid::regprocedure as function_signature,
  pg_get_userbyid(p.proowner) as owner,
  p.prosecdef as security_definer,
  p.proconfig as function_settings,
  pg_get_functiondef(p.oid) as definition
from pg_proc p
join pg_namespace n on n.oid = p.pronamespace
where n.nspname = any (/* scoped schemas */)
  and p.proname = any (/* flagged names */);
```

Check executable grants, caller identity binding, tenant or ownership guards, dynamic SQL, object qualification, and a safe `search_path`. A `SECURITY DEFINER` label is neither automatically safe nor automatically vulnerable.

Inspect views for invoker or definer behaviour, ownership, grants, and whether they expose data outside the intended RLS path.

## Supabase-specific cross-check

When Supabase is in scope:

- run the current Security Advisor and treat it as a lead;
- cross-check exposed schemas, table RLS state, policies, roles and grants directly;
- inspect `anon`, `authenticated`, service, support, migration, and custom-role paths that can reach the data;
- include Storage policies when the scoped access path uses them; and
- verify that service credentials or bypass roles are not exposed to untrusted clients.

Use the current [Supabase RLS guidance](https://supabase.com/docs/guides/database/postgres/row-level-security) and [Security Advisor documentation](https://supabase.com/docs/guides/database/database-advisors) for platform-specific behaviour.

## Effective-access verification

Prefer safe role simulation, dedicated test identities, transaction-wrapped checks, or application-equivalent requests over assumptions. Test allowed and denied operations separately for select, insert, update, and delete where they matter. Avoid reading or mutating real sensitive rows merely to prove access; use controlled fixtures or metadata evidence when possible.
