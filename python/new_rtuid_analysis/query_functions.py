#
import psycopg2

# database Connection
# -------------------------------------------------------------
def connection():
    try:
        #con = psycopg2.connect(database='v2bridge', user='lynn', host='localhost', port='5432')
        con = psycopg2.connect(database='v2bridge')
    except:
	return "Connection to DB Error"
    return con

# -------------------------------------------------------------
#   functions to find data for rtuid and config
# -------------------------------------------------------------
def find_configs_for_rtuid(rtuid,dbconn):
    cur = dbconn.cursor()
    sql = ("SELECT config_id,rtuid,major,minor"
            " FROM rtuid_config"
            " WHERE rtuid = %(rtuid)s"
    )
    try:
	cur.execute(sql,{'rtuid':rtuid})
    except:
        cur.close()
        return "Query error"

    rows = cur.fetchall()
    cur.close()
    return rows

# -------------------------------------------------------------
def find_pods_for_rtuid(rtuid,dbconn):
    cur = dbconn.cursor()
    sql = ("SELECT seq,rtuid,podid,major,minor"
            " FROM rtu_grouping"
            " WHERE rtuid = %(rtuid)s"
    )

    try:
	cur.execute(sql,{'rtuid':rtuid})
    except:
        cur.close()
        return "Query error"

    rows = cur.fetchall()
    cur.close()
    return rows

