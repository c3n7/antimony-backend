# Antimony Chat Backend

- Part of the `antimony chat project`.
- Built using `Python`, `Django` and `Django Rest Framework`.

### Dev Tip

To reset the tables whle developing, [do this](https://stackoverflow.com/a/3327326/7450617):

```sql
select 'drop table if exists "' || tablename || '" cascade;'
  from pg_tables
 where schemaname = 'public';
```

### License

```ascii
Antimony Chat Backend
Copyright (C) 2021  Timothy Karani

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published
by the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
```
