########
# Copyright (c) 2014 GigaSpaces Technologies Ltd. All rights reserved
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
#    * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    * See the License for the specific language governing permissions and
#    * limitations under the License.

from cloudify.decorators import operation
import os

__author__ = 'ENTER-AUTHOR-NAME-HERE'


@operation
def configure_resolv_conf(ctx,**kwargs):
    dns_ip = ctx.target.instance.host_ip
    # ctx.logger.info("HA SETUP {}    {}".format(dns_ip,node))
    ctx.source.instance.runtime_properties['work_with_dns'] = dns_ip
    s = 'nameserver {}'.format(dns_ip)
#   os.system("grep -q '{}' /etc/resolv.conf || sudo sed -i '1i {}' /etc/resolv.conf".format(s, s))
    ctx.logger.info("DNS SETUP {}".format(dns_ip))
    os.system("echo '{}' | sudo tee /etc/dnsmasq.resolv.conf".format(s))
    os.system("echo 'RESOLV_CONF=/etc/dnsmasq.resolv.conf' | sudo tee -a /etc/default/dnsmasq")
    os.system("sudo service dnsmasq restart")
    ctx.logger.info("DNS SETUP {}".format(s))
