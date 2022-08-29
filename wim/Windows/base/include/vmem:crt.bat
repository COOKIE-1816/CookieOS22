if not exist [DEFAULT FILES LOCATION] (
    mkdir [DEFAULT FILES LOCATION] >nul
) else (
    del [DEFAULT FILES LOCATION]\* >nul
    rmdir [DEFAULT FILES LOCATION] >nul

    mkdir [DEFAULT FILES LOCATION] >nul
)