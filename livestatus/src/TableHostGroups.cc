// +------------------------------------------------------------------+
// |             ____ _               _        __  __ _  __           |
// |            / ___| |__   ___  ___| | __   |  \/  | |/ /           |
// |           | |   | '_ \ / _ \/ __| |/ /   | |\/| | ' /            |
// |           | |___| | | |  __/ (__|   <    | |  | | . \            |
// |            \____|_| |_|\___|\___|_|\_\___|_|  |_|_|\_\           |
// |                                                                  |
// | Copyright Mathias Kettner 2014             mk@mathias-kettner.de |
// +------------------------------------------------------------------+
//
// This file is part of Check_MK.
// The official homepage is at http://mathias-kettner.de/check_mk.
//
// check_mk is free software;  you can redistribute it and/or modify it
// under the  terms of the  GNU General Public License  as published by
// the Free Software Foundation in version 2.  check_mk is  distributed
// in the hope that it will be useful, but WITHOUT ANY WARRANTY;  with-
// out even the implied warranty of  MERCHANTABILITY  or  FITNESS FOR A
// PARTICULAR PURPOSE. See the  GNU General Public License for more de-
// tails. You should have  received  a copy of the  GNU  General Public
// License along with GNU Make; see the file  COPYING.  If  not,  write
// to the Free Software Foundation, Inc., 51 Franklin St,  Fifth Floor,
// Boston, MA 02110-1301 USA.

#include "TableHostGroups.h"
#include <memory>
#include "Column.h"
#include "HostListColumn.h"
#include "HostListStateColumn.h"
#include "OffsetStringColumn.h"
#include "Query.h"
#include "auth.h"

using std::make_unique;
using std::string;

/* this might be a hack (accessing Nagios' internal structures.
   Hi Ethan: please help me here: how should this be code to be
   portable? */
extern hostgroup *hostgroup_list;

TableHostGroups::TableHostGroups(Logger *logger) : Table(logger) {
    addColumns(this, "", -1);
}

string TableHostGroups::name() const { return "hostgroups"; }

string TableHostGroups::namePrefix() const { return "hostgroup_"; }

// static
void TableHostGroups::addColumns(Table *table, const string &prefix,
                                 int indirect_offset) {
    hostgroup hgr;
    char *ref = reinterpret_cast<char *>(&hgr);
    table->addColumn(make_unique<OffsetStringColumn>(
        prefix + "name", "Name of the hostgroup",
        reinterpret_cast<char *>(&hgr.group_name) - ref, indirect_offset, -1,
        -1));
    table->addColumn(make_unique<OffsetStringColumn>(
        prefix + "alias", "An alias of the hostgroup",
        reinterpret_cast<char *>(&hgr.alias) - ref, indirect_offset, -1, -1));
    table->addColumn(make_unique<OffsetStringColumn>(
        prefix + "notes", "Optional notes to the hostgroup",
        reinterpret_cast<char *>(&hgr.notes) - ref, indirect_offset, -1, -1));
    table->addColumn(make_unique<OffsetStringColumn>(
        prefix + "notes_url",
        "An optional URL with further information about the hostgroup",
        reinterpret_cast<char *>(&hgr.notes_url) - ref, indirect_offset, -1,
        -1));
    table->addColumn(make_unique<OffsetStringColumn>(
        prefix + "action_url",
        "An optional URL to custom actions or information about the hostgroup",
        reinterpret_cast<char *>(&hgr.action_url) - ref, indirect_offset, -1,
        -1));
    table->addColumn(make_unique<HostListColumn>(
        prefix + "members",
        "A list of all host names that are members of the hostgroup",
        reinterpret_cast<char *>(&hgr.members) - ref, indirect_offset, false,
        -1, -1));
    table->addColumn(make_unique<HostListColumn>(
        prefix + "members_with_state",
        "A list of all host names that are members of the hostgroup together "
        "with state and has_been_checked",
        reinterpret_cast<char *>(&hgr.members) - ref, indirect_offset, true, -1,
        -1));

    table->addColumn(make_unique<HostListStateColumn>(
        prefix + "worst_host_state",
        "The worst state of all of the groups' hosts (UP <= UNREACHABLE <= "
        "DOWN)",
        HostListStateColumn::Type::worst_hst_state,
        reinterpret_cast<char *>(&hgr.members) - ref, indirect_offset, -1));
    table->addColumn(make_unique<HostListStateColumn>(
        prefix + "num_hosts", "The total number of hosts in the group",
        HostListStateColumn::Type::num_hst,
        reinterpret_cast<char *>(&hgr.members) - ref, indirect_offset, -1));
    table->addColumn(make_unique<HostListStateColumn>(
        prefix + "num_hosts_pending",
        "The number of hosts in the group that are pending",
        HostListStateColumn::Type::num_hst_pending,
        reinterpret_cast<char *>(&hgr.members) - ref, indirect_offset, -1));
    table->addColumn(make_unique<HostListStateColumn>(
        prefix + "num_hosts_up", "The number of hosts in the group that are up",
        HostListStateColumn::Type::num_hst_up,
        reinterpret_cast<char *>(&hgr.members) - ref, indirect_offset, -1));
    table->addColumn(make_unique<HostListStateColumn>(
        prefix + "num_hosts_down",
        "The number of hosts in the group that are down",
        HostListStateColumn::Type::num_hst_down,
        reinterpret_cast<char *>(&hgr.members) - ref, indirect_offset, -1));
    table->addColumn(make_unique<HostListStateColumn>(
        prefix + "num_hosts_unreach",
        "The number of hosts in the group that are unreachable",
        HostListStateColumn::Type::num_hst_unreach,
        reinterpret_cast<char *>(&hgr.members) - ref, indirect_offset, -1));

    table->addColumn(make_unique<HostListStateColumn>(
        prefix + "num_services",
        "The total number of services of hosts in this group",
        HostListStateColumn::Type::num_svc,
        reinterpret_cast<char *>(&hgr.members) - ref, indirect_offset, -1));

    // soft states
    table->addColumn(make_unique<HostListStateColumn>(
        prefix + "worst_service_state",
        "The worst state of all services that belong to a host of this group "
        "(OK <= WARN <= UNKNOWN <= CRIT)",
        HostListStateColumn::Type::worst_svc_state,
        reinterpret_cast<char *>(&hgr.members) - ref, indirect_offset, -1));
    table->addColumn(make_unique<HostListStateColumn>(
        prefix + "num_services_pending",
        "The total number of services with the state Pending of hosts in this "
        "group",
        HostListStateColumn::Type::num_svc_pending,
        reinterpret_cast<char *>(&hgr.members) - ref, indirect_offset, -1));
    table->addColumn(make_unique<HostListStateColumn>(
        prefix + "num_services_ok",
        "The total number of services with the state OK of hosts in this group",
        HostListStateColumn::Type::num_svc_ok,
        reinterpret_cast<char *>(&hgr.members) - ref, indirect_offset, -1));
    table->addColumn(make_unique<HostListStateColumn>(
        prefix + "num_services_warn",
        "The total number of services with the state WARN of hosts in this "
        "group",
        HostListStateColumn::Type::num_svc_warn,
        reinterpret_cast<char *>(&hgr.members) - ref, indirect_offset, -1));
    table->addColumn(make_unique<HostListStateColumn>(
        prefix + "num_services_crit",
        "The total number of services with the state CRIT of hosts in this "
        "group",
        HostListStateColumn::Type::num_svc_crit,
        reinterpret_cast<char *>(&hgr.members) - ref, indirect_offset, -1));
    table->addColumn(make_unique<HostListStateColumn>(
        prefix + "num_services_unknown",
        "The total number of services with the state UNKNOWN of hosts in this "
        "group",
        HostListStateColumn::Type::num_svc_unknown,
        reinterpret_cast<char *>(&hgr.members) - ref, indirect_offset, -1));

    // hard state
    table->addColumn(make_unique<HostListStateColumn>(
        prefix + "worst_service_hard_state",
        "The worst state of all services that belong to a host of this group "
        "(OK <= WARN <= UNKNOWN <= CRIT)",
        HostListStateColumn::Type::worst_svc_hard_state,
        reinterpret_cast<char *>(&hgr.members) - ref, indirect_offset, -1));
    table->addColumn(make_unique<HostListStateColumn>(
        prefix + "num_services_hard_ok",
        "The total number of services with the state OK of hosts in this group",
        HostListStateColumn::Type::num_svc_hard_ok,
        reinterpret_cast<char *>(&hgr.members) - ref, indirect_offset, -1));
    table->addColumn(make_unique<HostListStateColumn>(
        prefix + "num_services_hard_warn",
        "The total number of services with the state WARN of hosts in this "
        "group",
        HostListStateColumn::Type::num_svc_hard_warn,
        reinterpret_cast<char *>(&hgr.members) - ref, indirect_offset, -1));
    table->addColumn(make_unique<HostListStateColumn>(
        prefix + "num_services_hard_crit",
        "The total number of services with the state CRIT of hosts in this "
        "group",
        HostListStateColumn::Type::num_svc_hard_crit,
        reinterpret_cast<char *>(&hgr.members) - ref, indirect_offset, -1));
    table->addColumn(make_unique<HostListStateColumn>(
        prefix + "num_services_hard_unknown",
        "The total number of services with the state "
        "UNKNOWN of hosts in this group",
        HostListStateColumn::Type::num_svc_hard_unknown,
        reinterpret_cast<char *>(&hgr.members) - ref, indirect_offset, -1));
}

void TableHostGroups::answerQuery(Query *query) {
    for (hostgroup *hg = hostgroup_list; hg != nullptr; hg = hg->next) {
        if (!query->processDataset(hg)) {
            break;
        }
    }
}

void *TableHostGroups::findObject(const string &objectspec) {
    return find_hostgroup(const_cast<char *>(objectspec.c_str()));
}

bool TableHostGroups::isAuthorized(contact *ctc, void *data) {
    if (ctc == unknown_auth_user()) {
        return false;
    }

    hostgroup *hg = reinterpret_cast<hostgroup *>(data);
    for (hostsmember *mem = hg->members; mem != nullptr; mem = mem->next) {
        host *hst = mem->host_ptr;
        bool is = is_authorized_for(ctc, hst, nullptr);
        if (is && g_group_authorization == AuthorizationKind::loose) {
            return true;
        }
        if (!is && g_group_authorization == AuthorizationKind::strict) {
            return false;
        }
    }
    return true;
}
