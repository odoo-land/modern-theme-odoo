/** @odoo-module **/

import { Message } from '@mail/components/message/message';
import { session } from "@web/session";
import { patch } from 'web.utils';

const { useState } = owl;

var user = session.partner_id

patch(Message.prototype, 'modern_theme/static/src/components/message/message.js', {

    /**
     * Get the date time of the message at current user locale time.
     *
     * @returns {string}
     */
    get user_id() {
        return user;
    },
});
