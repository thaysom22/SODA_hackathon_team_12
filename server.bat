@echo off

setlocal
    for /F %%A in (.env) do set %%A

    flask run
endlocal
