/** @odoo-module **/

/**********************************************************************************
**********************************************************************************/

import { session } from "@web/session";
import { url } from "@web/core/utils/urls";
import { Dropdown } from "@web/core/dropdown/dropdown";

export class AppsMenu extends Dropdown {
    setup() {
    	super.setup();
    	this.env.bus.on("ACTION_MANAGER:UI-UPDATED", this, ev => this.close());
    }
}

Object.assign(AppsMenu, {
    template: 'modern_theme.AppsMenu',
});