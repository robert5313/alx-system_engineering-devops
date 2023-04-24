# Execute a command thats 
exec { 'pkill killmenow':
	path => '/usr/bin:/sbin:/bin'
}

