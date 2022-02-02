# Copyright © 2021 rdbende <rdbende@gmail.com>

source [file join [file dirname [info script]] MainFiles Light.tcl]
source [file join [file dirname [info script]] MainFiles Dark.tcl]

option add *tearOff 0

proc set_forest_theme {mode} {
	if {$mode == "dark"} {
		ttk::style theme use "forest-dark"
	} elseif {$mode == "light"} {
		ttk::style theme use "forest-light"
	}
}
