# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

from aliyunsdkcore.request import RpcRequest
from aliyunsdkvpc.endpoint import endpoint_data

class AssociatePhysicalConnectionToVirtualBorderRouterRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Vpc', '2016-04-28', 'AssociatePhysicalConnectionToVirtualBorderRouter','Vpc')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_ResourceOwnerId(self):
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self,ResourceOwnerId):
		self.add_query_param('ResourceOwnerId',ResourceOwnerId)

	def get_CircuitCode(self):
		return self.get_query_params().get('CircuitCode')

	def set_CircuitCode(self,CircuitCode):
		self.add_query_param('CircuitCode',CircuitCode)

	def get_VlanId(self):
		return self.get_query_params().get('VlanId')

	def set_VlanId(self,VlanId):
		self.add_query_param('VlanId',VlanId)

	def get_ClientToken(self):
		return self.get_query_params().get('ClientToken')

	def set_ClientToken(self,ClientToken):
		self.add_query_param('ClientToken',ClientToken)

	def get_VbrId(self):
		return self.get_query_params().get('VbrId')

	def set_VbrId(self,VbrId):
		self.add_query_param('VbrId',VbrId)

	def get_PeerGatewayIp(self):
		return self.get_query_params().get('PeerGatewayIp')

	def set_PeerGatewayIp(self,PeerGatewayIp):
		self.add_query_param('PeerGatewayIp',PeerGatewayIp)

	def get_PeeringSubnetMask(self):
		return self.get_query_params().get('PeeringSubnetMask')

	def set_PeeringSubnetMask(self,PeeringSubnetMask):
		self.add_query_param('PeeringSubnetMask',PeeringSubnetMask)

	def get_LocalGatewayIp(self):
		return self.get_query_params().get('LocalGatewayIp')

	def set_LocalGatewayIp(self,LocalGatewayIp):
		self.add_query_param('LocalGatewayIp',LocalGatewayIp)

	def get_ResourceOwnerAccount(self):
		return self.get_query_params().get('ResourceOwnerAccount')

	def set_ResourceOwnerAccount(self,ResourceOwnerAccount):
		self.add_query_param('ResourceOwnerAccount',ResourceOwnerAccount)

	def get_OwnerAccount(self):
		return self.get_query_params().get('OwnerAccount')

	def set_OwnerAccount(self,OwnerAccount):
		self.add_query_param('OwnerAccount',OwnerAccount)

	def get_OwnerId(self):
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self,OwnerId):
		self.add_query_param('OwnerId',OwnerId)

	def get_PhysicalConnectionId(self):
		return self.get_query_params().get('PhysicalConnectionId')

	def set_PhysicalConnectionId(self,PhysicalConnectionId):
		self.add_query_param('PhysicalConnectionId',PhysicalConnectionId)