
from utils.fdate import fdate
from utils.variables_locales import add_variable_local

CWD = None

# - Añadimos variables de entorno locales de fechas comunes
add_variable_local("DATE_YYYY-MM-DD", fdate("%Y-%m-%d"))
add_variable_local("DATE_YYYYMMDD", fdate("%Y%m%d"))
add_variable_local("DATE_R1D_YYYY-MM-DD", fdate("%Y-%m-%d", -1))
add_variable_local("DATE_R1D_YYYYMMDD", fdate("%Y%m%d", -1))

# - Filtros usados en informes de SMS
add_variable_local("DATE_R4D_YYYYMMDD", fdate("%Y%m%d", -4))
add_variable_local("DATE_R4D_YYYY-MM-DD", fdate("%Y-%m-%d", -4))
add_variable_local("DATE_R25D_YYYY-MM-DD", fdate("%Y-%m-%d", -25))
add_variable_local("DATE_R26D_YYYY-MM-DD", fdate("%Y-%m-%d", -26))
add_variable_local("DATE_R50D_YYYY-MM-DD", fdate("%Y-%m-%d", -50))
add_variable_local("DATE_R51D_YYYY-MM-DD", fdate("%Y-%m-%d", -51))
add_variable_local("DATE_R75D_YYYY-MM-DD", fdate("%Y-%m-%d", -75))
add_variable_local("DATE_R76D_YYYY-MM-DD", fdate("%Y-%m-%d", -76))
add_variable_local("DATE_R100D_YYYY-MM-DD", fdate("%Y-%m-%d", -100))

# - Filtros DD-MM-YYYY
add_variable_local("DATE_R30D_DD-MM-YYYY", fdate("%d-%m-%Y", -30))