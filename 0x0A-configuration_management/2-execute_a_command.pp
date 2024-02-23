# termination file named killmenow
exec { 'p_killmenow':
    command => '/bin/pkill -15 killmenow;'
}
