#version 330 core

uniform	mat4 view_model;
uniform	mat4 many_view_model[200];
uniform	mat4 projection;

layout(location = 0) in vec3 vPosition;
layout(location = 1) in vec2 textCoords;
layout(location = 2) in vec3 NormalCoords;

in vec3 position;

out vec2 outText;
out vec3 position1;
out vec3 normal;

void main ()
{
	position1 = vec3(many_view_model[gl_InstanceID] * vec4(vPosition, 1));
	normal = vec3(many_view_model[gl_InstanceID] * vec4(NormalCoords, 0));
	outText = textCoords;

	gl_Position = projection * many_view_model[gl_InstanceID] * vec4(vPosition, 1.0f);

//	texCoord = vec2(vTexCoord.s, 1.0 - vTexCoord.t);
//	gl_Position = projectionMatrix * modelViewMatrix * vec4 (vPosition, 1);

}

