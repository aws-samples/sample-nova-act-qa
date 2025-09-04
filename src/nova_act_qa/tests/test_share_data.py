# Copyright Amazon Inc

# Licensed under the MIT License (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://opensource.org/licenses/MIT
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
The tests in this file demonstrate how to share data between tests using pytest's built-in cache
and @pytest.mark.xdist_group to ensure tests run sequentially on the same worker process.
"""

from pydantic import BaseModel
import pytest
from nova_act_qa.utils.nova_act import NovaAct

# Expected Blog Post name to assert
expected_blog_post_title = "Useful, reliable agents from prototype to production"
expected_blog_post_author = "Amazon AGI"
expected_blog_post_date = "July 16, 2025"


# Schema of the data to extract
class BlogDetailsSchema(BaseModel):
    title: str
    author: str
    date: str


# Name of the cache key to store the data in
blog_post_cache_key = "blog_post_details"

# Name of xdist group to run tests sequentially on same worker
xdist_group_name = "share_data"


@pytest.mark.xdist_group(xdist_group_name)
@pytest.mark.parametrize(
    "nova", ["https://labs.amazon.science/blog/prototype-to-production"], indirect=True
)
def test_extract_data(nova: NovaAct, pytestconfig: pytest.Config):
    """First test that extracts and stores shared data."""

    # Extract the data
    result = nova.act(
        "Get the Blog Post title", schema=BlogDetailsSchema.model_json_schema()
    )
    data = nova.is_result_valid(result)
    blog_post_details = BlogDetailsSchema.model_validate(data)

    # Assert the data
    assert expected_blog_post_title == blog_post_details.title
    assert expected_blog_post_author == blog_post_details.author
    assert expected_blog_post_date == blog_post_details.date

    # Store the data for the second test to use
    pytestconfig.cache.set(blog_post_cache_key, blog_post_details.model_dump_json())


@pytest.mark.xdist_group(xdist_group_name="share_data")
@pytest.mark.parametrize("nova", ["https://labs.amazon.science"], indirect=True)
def test_consume_data(nova: NovaAct, pytestconfig: pytest.Config):
    """Second test that uses the shared data from the first test."""

    nova.act("Go to the Blog page")

    # Get the data from the previous test
    cached_blog_post_details = pytestconfig.cache.get(blog_post_cache_key, "{}")
    blog_post_details = BlogDetailsSchema.model_validate_json(cached_blog_post_details)

    # Use the data
    nova.act(
        f"Select the Blog Post {blog_post_details.title} by {blog_post_details.author} on {blog_post_details.date}"
    )
    nova.test_bool(f"Blog Post {blog_post_details.title} is displayed")
