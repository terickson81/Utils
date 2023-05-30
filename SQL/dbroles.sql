USE YourDatabaseName;
SELECT 
    r.name AS RoleName,
    m.name AS MemberName,
    dp.type_desc AS MemberType
FROM 
    sys.database_role_members drm
    JOIN sys.database_principals r ON drm.role_principal_id = r.principal_id
    JOIN sys.database_principals m ON drm.member_principal_id = m.principal_id
    JOIN sys.database_principals dp ON m.sid = dp.sid;
